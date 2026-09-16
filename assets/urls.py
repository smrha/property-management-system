from django.urls import path
from . import views

app_name = "assets"

urlpatterns = [
    path('list/', views.assets_list_view, name='assets_list'),
    path('create/', views.assets_create_view, name='assets_create'),
    path("<int:id>/", views.asset_detail_view, name="assets_detail"),
]