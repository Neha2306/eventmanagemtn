from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .userdata import CustomUserCreationForm
from .models import Event
from .serializers import EventSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from datetime import datetime
import requests
from django.http import HttpRequest
import json
from django.http import HttpResponse
import calendar
# Create your views here.

def userLogoutView(request):
    logout(request)
    return redirect('index')

def redirect_authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
    
@login_required
def index(request):
    user = request.user
    search_event_name = ''
    search_date = ''
    search_location = ''
    sortby = ''
    if request.GET.get('serachevent') is not None:
        search_event_name = request.GET.get('serachevent')
    if request.GET.get('datefilter') is not None:
        search_date = request.GET.get('datefilter')
    if request.GET.get('filterlocation') is not None:
        search_location = request.GET.get('filterlocation')
    if request.GET.get('sortby') is not None:
        sortby = request.GET.get('sortby')
    locations = Event.objects.values('location').distinct()
    unacceptedrsvpevents = Event.objects.filter(isrsvp=True).exclude(rsvp_users=request.user).exclude(organizer=request.user.id)
    acceptedrsvpevents = Event.objects.filter(rsvp_users__id=request.user.id, isrsvp=True).exclude(organizer=request.user.id)
    casualeventinvitations = Event.objects.filter(rsvp_users__id=request.user.id, isrsvp=False).exclude(organizer=request.user.id)
    if search_event_name:
        unacceptedrsvpevents = unacceptedrsvpevents.filter(title__icontains=search_event_name)
        acceptedrsvpevents = acceptedrsvpevents.filter(title__icontains=search_event_name)
        casualeventinvitations = casualeventinvitations.filter(title__icontains=search_event_name)
    if search_date:
        unacceptedrsvpevents = unacceptedrsvpevents.filter(date=search_date)
        acceptedrsvpevents = acceptedrsvpevents.filter(date=search_date)
        casualeventinvitations = casualeventinvitations.filter(date=search_date)
    if search_location:
        unacceptedrsvpevents = unacceptedrsvpevents.filter(location__icontains=search_location)
        acceptedrsvpevents = acceptedrsvpevents.filter(location__icontains=search_location)
        casualeventinvitations = casualeventinvitations.filter(location__icontains=search_location)
    if sortby:
        unacceptedrsvpevents = unacceptedrsvpevents.order_by(sortby.replace("sort", ""))
        acceptedrsvpevents = acceptedrsvpevents.order_by(sortby.replace("sort", ""))
        casualeventinvitations = casualeventinvitations.order_by(sortby.replace("sort", ""))
    return render(request, 'home.html', context={'user':user, 'unacceptedrsvpevents':unacceptedrsvpevents, 'acceptedrsvpevents':acceptedrsvpevents, 'casualeventinvitations':casualeventinvitations, 'locations':locations, 'search_event_name': search_event_name, 'search_date':search_date, 'search_location':search_location, 'sortby':sortby})

@redirect_authenticated_user
def userRegistrationView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registration.html', context={'form':form})

class userLoginView(LoginView):
    redirect_authenticated_user = True
    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

class EventModelViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

@login_required
def ViewCreatedEvents(request):
    user = request.user
    events = Event.objects.filter(organizer=request.user.id)
    return render(request, 'view_created_events.html', context={'events':events})

@login_required
def AddNewEvent(request):
    user = request.user
    users = User.objects.exclude(id=request.user.id)
    context = {
                'user':user,
                'users':users,
                'title':'',
                'description':'',
                'event_date':'',
                'event_time':'',
                'rsvp_users_ids':[],
                'error':'',
                'success':'',
                'isrsvp': ''
            }
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        event_date = request.POST.get('eventdate')
        event_time = request.POST.get('eventtime')
        location = request.POST.get('location')
        rsvp_users_ids = request.POST.getlist('selectrsvpusers')
        isrsvp = request.POST.get('isrsvp')
        if isrsvp is not None and isrsvp == 'on':
            isrsvp = True
        else:
            isrsvp = False
        context['title'] = title
        context['description'] = description
        context['event_date'] = event_date
        context['event_time'] = event_time
        context['location'] = location
        context['rsvp_users_ids'] = rsvp_users_ids
        context['isrsvp'] = isrsvp
        if title and description and event_date and event_time and location:
            try:
                event_date = datetime.strptime(event_date, '%Y-%m-%d').date()
                event_time = datetime.strptime(event_time, '%H:%M').time()
            except ValueError:
                context['error'] = 'Invalid date or time format'
                context['success'] = ''
                return render(request, 'add_new_event.html', context)

            try:
                event = Event(
                    title = title,
                    description = description,
                    date = event_date,
                    time = event_time,
                    location = location,
                    organizer = User.objects.get(pk=request.user.id),
                    isrsvp = isrsvp
                )
                
                event.save()
                event.rsvp_users.add(*rsvp_users_ids)

                context['success'] = 'Event Successfully Created'
                context['error'] = ''
                context['title'] = ''
                context['description'] = ''
                context['event_date'] = ''
                context['event_time'] = ''
                context['location'] = ''
                context['rsvp_users_ids'] = ''
                context['isrsvp'] = ''
            except:
                context['error'] = 'Something went Wrong. Please Try again.'
                context['success'] = ''
            return render(request, 'add_new_event.html', context)
        else:
            context['error'] = 'All fields are required'
            context['success'] = ''
            return render(request, 'add_new_event.html', context)
    else:
        return render(request, 'add_new_event.html', context)

@login_required
def deleteEvent(request, event_id):
    domain_url = request.scheme + '://' + request.get_host()
    url = f"{domain_url}/api/v1/events/{event_id}/"
    response = requests.delete(url)
    return redirect('viewevents')

@login_required
def rsvpEventConfirmation(request, event_id, user_id):
    event = Event.objects.get(pk=event_id)
    event.rsvp_users.add(User.objects.get(pk=user_id))
    event.save()
    return redirect('index')
 
@login_required
def editEvent(request, event_id):
    user = request.user
    users = User.objects.exclude(id=request.user.id)
    event = Event.objects.get(pk=event_id)
    rsvp_users = event.rsvp_users.all()
    rsvp_user_ids = [str(user.id) for user in rsvp_users]
    context = {
                'user':user,
                'users':users,
                'event':event,
                'rsvp_users': rsvp_user_ids,
                'error':'',
                'success':''
            }
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        event_date = request.POST.get('eventdate')
        event_time = request.POST.get('eventtime')
        location = request.POST.get('location')
        rsvp_users_ids = request.POST.getlist('selectrsvpusers')
        isrsvp = request.POST.get('isrsvp')
        if isrsvp is not None and isrsvp == 'on':
            isrsvp = True
        else:
            isrsvp = False
        if title and description and event_date and event_time and location:
            try:
                domain_url = request.scheme + '://' + request.get_host()
                url = f"{domain_url}/api/v1/events/{event_id}/"
                payload = json.dumps({
                    "organizer": request.user.id,
                    "rsvp_users": rsvp_users_ids,
                    "title": title,
                    "description": description,
                    "date": event_date,
                    "time": event_time,
                    "location": location,
                    "isrsvp": isrsvp
                })
                headers = {
                    'Content-Type': 'application/json'
                }
                requests.request("PUT", url, headers=headers, data=payload)
                context['success'] = 'Event Successfully Created'
                context['error'] = ''
                event = Event.objects.get(pk=event_id)
                rsvp_users = event.rsvp_users.all()
                rsvp_user_ids = [str(user.id) for user in rsvp_users]
                context['event'] = event
                context['rsvp_users'] = rsvp_user_ids
            except Exception as e:
                context['error'] = e
                context['success'] = ''

            return render(request, 'edit_event.html', context)
        else:
            context['error'] = 'All fields are required'
            context['success'] = ''
            return render(request, 'edit_event.html', context)
    else:
        return render(request, 'edit_event.html', context)

@login_required
def viewRsvpAcceptedUser(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'view_event_rsvp_users.html', context={'event':event})

@login_required
def processRsvpEventsCalendarView(request, year=None, month=None):
    today = datetime.today()
    if year is None or month is None:
        year, month = today.year, today.month
    else:
        year, month = int(year), int(month)
    
    prev_month = month - 1 if month > 1 else 12
    prev_year = year - 1 if month == 1 else year
    next_month = month + 1 if month < 12 else 1
    next_year = year + 1 if month == 12 else year

    num_days = calendar.monthrange(year, month)[1]
    days_list = list(range(1, num_days + 1))

    events = Event.objects.filter(date__year=year, date__month=month, rsvp_users__id=request.user.id, isrsvp=True)
    events = events.exclude(organizer=request.user.id)
    
    return render(request, 'event_calendar.html', {
        'events': events,
        'year': year,
        'month': month,
        'prev_month': prev_month,
        'prev_year': prev_year,
        'next_month': next_month,
        'next_year': next_year,
        'days_list': days_list,
        'today':today
    })