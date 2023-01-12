from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_products),
    path('manage/',views.create_product),
    path('manage/<int:pk>/', views.manage_product)
]