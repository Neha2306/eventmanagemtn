from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200, null=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    rsvp_users = models.ManyToManyField(User, related_name='rsvps', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    isrsvp = models.BooleanField(default=False)

    def __str__(self):
        return self.title
