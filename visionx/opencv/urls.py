from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='opencv-home'),
    path('about/', views.about, name='opencv-about'),

]