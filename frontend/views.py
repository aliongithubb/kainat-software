from django.shortcuts import render
from urllib import request
from django.views import View
from django.conf import settings
import pywhatkit as wt
from datetime import datetime
from .models import *
from accounts.models import *

# Create your views here.

"""
##================================##
##    Landing Page View Class     ##
##================================##

"""
class Landing(View):
    # Get Function Of Landing Class
    def get(self, request):
        profile_type = request.session.get('profile_type')
        profile_email = request.session.get('profile_email')
        if profile_email and profile_type:
            if profile_type == 'user':
                profile = User.objects.filter(email=profile_email).first()
            elif profile_type == 'customer':
                profile = Customer.objects.filter(email=profile_email).first()
            elif profile_type == 'vendor':
                profile = User.objects.filter(email=profile_email).first()
            data = {
            'profile': profile
            }
            return render(request, 'index.html', data)
        else:
            return render(request, 'index.html')
    # Post Function Of Landing Class
    def post(self, request):
        return render(request, 'index.html')

"""
##==============================##
##    About Page View Class     ##
##==============================##

"""
class About(View):
    # Get Function of About Class
    def get(self, request):
        return render(request, 'about.html')


"""
##===================================##
##    Contact Us Page View Class     ##
##===================================##

"""
class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')



"""
##===================================##
##    Profile setting Page View Class     ##
##===================================##

"""
class Profile_Setting(View):
    def get(self, request):
        return render(request, 'profile_setting.html')



"""
##==================================##
##    Dashboard Page View Class     ##
##==================================##

"""
class Dashboard(View):
    def get(self, request):
        return render(request, 'dashboard/admin-index.html')

    