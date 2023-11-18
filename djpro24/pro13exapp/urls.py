from django.urls import path
from pro13exapp import views

urlpatterns = [
    path('buserlist', views.BuserShow),
    path('jikwonlist', views.JikwonShow),
    path('gogeklist', views.GogekShow),


]
