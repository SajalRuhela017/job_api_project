from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_job, name='add_job'),
    path('all', views.get_jobs, name='get_jobs'),
    path('remove', views.remove_job, name='remove_job'),
]