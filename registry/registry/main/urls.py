from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('change/<int:id>/', views.change, name='change'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
