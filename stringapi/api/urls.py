from django.urls import path
from .views import string_reverse

urlpatterns = [
    path('reverse/<str:input_string>/', string_reverse , name='string_reverse'),
]