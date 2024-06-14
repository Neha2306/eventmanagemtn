from django.urls import path, include
from .views import userRegistrationView, index, userLoginView, userLogoutView, ViewCreatedEvents, AddNewEvent, deleteEvent, editEvent, rsvpEventConfirmation, viewRsvpAcceptedUser, processRsvpEventsCalendarView
from django.conf import settings
from django.conf.urls.static import static
from .views import EventModelViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'events', EventModelViewSet)

urlpatterns = [
    path("", index, name='index'),
    path('accounts/registration/', userRegistrationView),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', userLoginView.as_view(), name='login'),
    path('logout/', userLogoutView, name='logout'),
    path('api/v1/', include(router.urls)),
    path("view_events", ViewCreatedEvents, name='viewevents'),
    path("add_new_event", AddNewEvent, name='addnewevent'),
    path('delete_event/<int:event_id>/', deleteEvent, name='deleteevent'),
    path('edit_event/<int:event_id>/', editEvent, name='editevent'),
    path('rsvp_event_confirmation/<int:event_id>/<int:user_id>/', rsvpEventConfirmation, name='rsvpeventconfirmation'),
    path('view_event_rsvp_users/<int:event_id>', viewRsvpAcceptedUser, name='vieweventrsvpusers'),
    path('view-rsvp-event-calendar/', processRsvpEventsCalendarView, name='viewrsvpeventcalendar'),
    path('view-rsvp-event-calendar/<int:year>/<int:month>/', processRsvpEventsCalendarView, name='viewrsvpeventcalendar'),
] + static(settings.STATIC_URL)