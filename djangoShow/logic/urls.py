from django.urls import path
from .views import *

app_name = 'logic'
urlpatterns = [
    # стартовая
    path('', start_page, name='start_page'),
]