from django.urls import path
from . import views

urlpatterns = [
    path('accept_request', views.accept_request ,name = 'accept_request')
]
