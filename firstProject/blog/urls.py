from django.urls import path
from . import views
urlpatterns = [
    path('', views.vMain, name='main-page'),
]