from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home),
    path('discusion/<str:pk>/',discusion, name='discusion')
]