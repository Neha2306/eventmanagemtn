from rest_framework import serializers
from .models import Event
from django.contrib.auth.models import User

class EventSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    organizer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=True, required=True)
    rsvp_users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, allow_null=True, required=True)
    class Meta:
        model = Event
        fields = '__all__'
 