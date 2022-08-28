from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('cyclist',views.cyclist_project,name='cyclist'),
    path('sentimenter',views.sentimenter,name='sentimenter'),
    path('sentimenter_plain',views.sentimenter_plain,name='sentimenter_plain'),
    path('spammer_plain',views.spammer_plain,name='spammer_plain'),
    path('spammer',views.spammer,name='spammer')
]