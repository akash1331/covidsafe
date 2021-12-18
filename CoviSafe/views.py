from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.serializers import Serializer
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets
from IARE.seralizers import *
from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model # If used custom user model
from django.contrib.auth.models import User

# from django.contrib.auth import authnticate,login,logout

class profileApi(APIView):
    def get(self,request):
        profile1 = citizen.objects.all()
        serializer = CitizenSerializer(profile1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

# class traceApi(APIView):
#     def get(self,request):
#         trace = citizen.objects.all()
#         serializer = CitizenSerializer(profile1,many=True)
#         return Response(serializer.data)

#     def post(self):
#         pass

# @api_view(['GET'])
class loginview(APIView):
    authentication_classes = [BasicAuthentication,SessionAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,format=None):
        content ={
            'user':str(request.user),
            'auth':str(request.auth),
            # 'token':str(request.token),
        }
        return Response(content)


class registerView(APIView):
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return Response(user)
    