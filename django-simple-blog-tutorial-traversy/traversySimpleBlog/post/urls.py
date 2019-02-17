from django.urls import path
from post import views

app_name = 'post'

urlpatterns = [
  path('', views.index, name='index'),
  path('details/<int:id>/', views.details, name='details'),
]