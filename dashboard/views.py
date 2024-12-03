from django.shortcuts import render
from django.views import View
# Create your views here.

"""
##==================================##
##    Dashboard Page View Class     ##
##==================================##

"""
class Dashboard(View):
    def get(self, request):
        return render(request, 'dashboard.html')
