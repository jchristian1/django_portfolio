from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('cyclist',views.cyclist_project,name='cyclist'),
    path('sentimenter',views.sentimenter,name='sentimenter'),
    path('spammer',views.spammer,name='spammer')
]