from django.urls import path
from .views import *

app_name = 'appeals'
urlpatterns = [
    path('', index, name='index'),
    path('add_complaint/', add_complaint, name='add_complaint'),
]