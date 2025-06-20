from rest_framework import serializers
from .models import CustomUser, Categories, NeworPopular

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class UserCreateSerailizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name']

# class UserCreateSerailizer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)   # we never want to return it back in API responses, even after registration.
#                                                         # You can write (send) it from the frontend.  But it will not be shown in API responses.

#     class Meta:
#         model = CustomUser
#         fields = ['id', 'email', 'name', 'password']

#     def create(self, validated_data):
#         return CustomUser.objects.create_user(
#             email = validated_data['email'],
#             name = validated_data['name'],
#             password = validated_data['password']
#         )

class CategorySerailizer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class NeworPuSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeworPopular
        fields = '__all__'