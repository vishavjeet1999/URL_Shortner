from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('short/', short),
    path('<int:id>', urlshort)
]
