from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('query/', views.query, name='query'),
    path('query/empty/', views.empty_database, name='empty')
]