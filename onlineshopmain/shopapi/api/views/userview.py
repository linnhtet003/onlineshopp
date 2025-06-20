from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from ..models import CustomUser
from ..serializers import UserSerializer, UserCreateSerailizer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import AllowAny

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

class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        name = request.data.get('name')
        password = request.data.get('password')

        if CustomUser.objects.filter(email = email).exists():
            return Response({'error': 'Your email is already taken'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.create_user(
                email = email,
                name = name,
                password = password
            )

            refresh = RefreshToken.for_user(user)
            serializer = UserCreateSerailizer(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# class RegisterUser(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = UserCreateSerailizer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             token, _= Token.objects.get_or_create(user=user)    #  _: a boolean (True if it was created, False if already existed — we ignore it using _).
#             return Response({'token': token.key}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)