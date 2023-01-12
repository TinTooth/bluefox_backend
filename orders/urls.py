from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_create),
    path('<int:pk>/', views.manage),
]