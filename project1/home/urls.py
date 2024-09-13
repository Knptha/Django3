from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('About/', views.About, name='About'),
    path('Contact/', views.Contact, name='Contact'),


]