from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('add/', views.submit_resource, name='add_resource'),
    path('edit/<int:resource_id>/', views.edit_resource, name='edit_resource'),
    path('delete/<int:resource_id>/', views.delete_resource, name='delete_resource'),
]
