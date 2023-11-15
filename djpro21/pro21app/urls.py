from django.urls import path
from pro21app import views

urlpatterns = [
    path('survey', views.surveyView),
    path('surveyshow', views.surveyAnalysis),
    path('surveyprocess', views.surveyProcess),
]
