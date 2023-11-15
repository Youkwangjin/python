
from django.contrib import admin
from django.urls import path, include
from pro21app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.surveyMain),
    path('coffee/', include('pro21app.urls')),

    
]
