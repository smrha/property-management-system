from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.assets_list_view, name='assets_list'),
]