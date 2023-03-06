from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.inventory_home, name='inventory_home'),

]