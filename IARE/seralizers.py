from django.db.models import fields
from rest_framework import serializers
from CoviSafe.models import *
from django.contrib.auth import get_user_model # If used custom user model


class CitizenSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField(max_length=30)
    # last_name = serializers.CharField(max_length=30)
    # profile_photo = serializers.ImageField(default = False)

    class Meta:
        model = citizen
        fields = '__all__'


# UserModel = get_user_model

# class registerSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only = True)

#     def create(self,validated_data):
#         user = UserModel.objects.create_user(
#             username=validated_data['username'],
#             password=validated_data['password'],
#         )
#         return user

#     class Meta:
#         model = UserModel
#         fields = ("username", "password")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = citizen
        fields = ('username', 'password','first_name', 'last_name')
        write_only_fields = ('password',)

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = citizen
        fields = ('username','password','key')