from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delete_conf/<int:id>/', views.delete_conf, name='delete_conf'),
    path('create', views.create, name='create'),
    path('change/<int:id>/', views.change, name='change'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
