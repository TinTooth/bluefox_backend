from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_options),
    path('manage/', views.create_option),
    path('manage/<int:pk>/', views.manage_option),
]