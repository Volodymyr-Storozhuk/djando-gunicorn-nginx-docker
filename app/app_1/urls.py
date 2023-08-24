from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_app, name='hello_app_page'),
]
