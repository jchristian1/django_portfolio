from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('cyclist',views.cyclist_project,name='cyclist')
]