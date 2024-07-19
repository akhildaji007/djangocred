from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/', views.item_list, name='item_list'),
    path('items/create/', views.item_create, name='item_create'),
    path('items/<pk>/update/', views.item_edit, name='item_update'),
    path('items/<pk>/delete/', views.item_delete, name='item_delete'),
]