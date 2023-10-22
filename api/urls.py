from django.urls import path
from . import views 
from .serializers import ItemSerializer
urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem)
] 