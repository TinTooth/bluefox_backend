from django.urls import path
from . import views

urlpatterns = [
    path('', views.create),
    path('get', views.get_all),
    path('<int:pk>/', views.manage),
    path('put/<int:pk>/', views.update),
]