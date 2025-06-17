from django.urls import path
from .views.userview import UserList

urlpatterns = [
    path('userlist/', UserList.as_view(), name='user_list'),
]
