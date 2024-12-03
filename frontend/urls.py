from django.urls import path
from .views import *

app_name = 'frontend'

urlpatterns = [
    path('', Landing.as_view(), name='landing_page'),
    path('about/', About.as_view(), name='about page'),
    path('contact/', Contact.as_view(), name='contact page'),
    path('setting/', Profile_Setting.as_view(), name='profile setting'),

]