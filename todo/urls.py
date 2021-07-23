from django.urls import path
from . import views

urlpatterns = [
    path('', views.list),
    path('<int:todo_id>/', views.detail),
    path('add/', views.add),
    path('<int:todo_id>/edit/', views.edit),
    path('<int:todo_id>/delete/', views.delete),
]