from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from ..models import CustomUser
from ..serializers import UserSerializer
from rest_framework.response import Response

# Create your views here.

class UserList(APIView):
    authentication_classes = (TokenAuthentication,) # [TokenAuthentication]
    def get(self,request):
        users = CustomUser.objects.all()
        data = []
        for user in users:
            serializer = UserSerializer(user)
            data.append(serializer.data)
        return Response(data)