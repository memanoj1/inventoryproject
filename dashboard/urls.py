from re import I
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='Dashboard-index'),
    path('staff/', views.staff, name="Dashboard-staff"),
    path('product/', views.product, name='Dashboard-product'),
    path('order/',views.order, name='Dashboard-order'),
]

