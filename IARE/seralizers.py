from django.db.models import fields
from rest_framework import serializers
from CoviSafe.models import *

class CitizenSerializer(serializers.Serializer):
    first_name = serializers.TextField(max_length=30)
    last_name = serializers.TextField(max_length=30)
    profile_photo = serializers.ImageField(default = False)