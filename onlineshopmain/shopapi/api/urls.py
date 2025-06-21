from django.urls import path
from .views.userview import UserList, RegisterUser
from .views.categoryview import Category, CategoryCreate, CategoryUpdate, CategoryDelete
from .views.neworpopularview import neworpupular, neworpupularCreate, neworpupularUpdate, neworpupularDelete
from .views.productview import ProductsList, ProductCreate, ProductDetail, ProductUpdate, ProductDelete

urlpatterns = [
    path('userlist/', UserList.as_view(), name='user_list'),
    path('register/', RegisterUser.as_view(), name='register_user'),

    # Category
    path('categorylist/', Category.as_view(), name='category_list'),
    path('categorycreate/', CategoryCreate.as_view(), name='category_create'),
    path('categoryupdate/<int:pk>/', CategoryUpdate.as_view(), name='category_update'),
    path('categorydelete/<int:pk>/', CategoryDelete.as_view(), name='category_delete'),

    # NeworPopular
    path('neworpolist/', neworpupular.as_view(), name='neworpo_list'),
    path('neworpocreate/', neworpupularCreate.as_view(), name='neworpo_create'),
    path('neworpoupdate/<int:pk>/', neworpupularUpdate.as_view(), name='neworpo_update'),
    path('neworpodelete/<int:pk>/', neworpupularDelete.as_view(), name='neworpo_delete'),

    # Products
    path('productlist/', ProductsList.as_view(), name='product_list'),
    path('productcreate/', ProductCreate.as_view(), name='product_create'),
    path('productdetail/<int:pk>/', ProductDetail.as_view(), name='product_update'),
    path('productupdate/<int:pk>/', ProductUpdate.as_view(), name='product_update'),
    path('productdelete/<int:pk>/', ProductDelete.as_view(), name='product_delete'),
]