from django.urls import path
from .views.userview import UserList, RegisterUser

urlpatterns = [
    path('userlist/', UserList.as_view(), name='user_list'),
    path('register/', RegisterUser.as_view(), name='register_user'),
]