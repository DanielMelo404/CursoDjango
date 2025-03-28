from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('discusion/<str:pk>/',discusion, name='discusion'),
    path('crear_discusion/', crear_discusion, name='crear-discusion'),
    path('update_discusion/<str:pk>/', update_discusion, name='update-discusion')
]