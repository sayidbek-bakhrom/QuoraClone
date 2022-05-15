from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('add-question/', views.AddQuestionView.as_view(), name='add-question'),
    path('respond/<slug:slug>/', views.RespondQuestionView.as_view(), name='respond-question')
]