from django.urls import path, include
from snippets import views

urlpatterns = [
    path('', views.index, name='index'),
]