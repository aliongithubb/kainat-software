from django.shortcuts import render, redirect
from urllib import request
from django.views import View
from django.conf import settings
from .models import *
from .utils import *
import pywhatkit as wt
from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password
import random

# Create your views here.

"""
##=====================================##
##    Registration Page View Class     ##
##======================================##

"""


class Registration(View):
    # Get Function For Registration Class
    def get(self, request):
        user = User.objects.all()
        if not user:
            user = User(
                first_name='Fayyaz ali',
                last_name='M Riaz Mughal',
                email='fayyazali100@gmail.com',
                phone_number='00923224704244',
                password=make_password('12345678'),
                bio='',
                address='',
                city='',
                country='',
                email_otp='123456',
                phone_otp='123456',
                email_verified=True,
                phone_verified=True,
                is_delete=False,
                group='admin'
            )
            user.save()
            create_user_activity(user, 'user')
        # return render(request, 'business-setting.html')
        return render(request, 'registration.html')

    # Post Function for Registration Class
    def post(self, request):

        # Define Data for template
        data = {}

        # Getting Input from user to add data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Data Validate provided by the user
        if len(first_name) < 3:
            data['first_name_error'] = 'Please enter the first name'
        elif len(last_name) < 3:
            data['last_name_error'] = 'Please enter the last name'
        elif not phone_number:
            data['phone_number_error'] = 'Please enter a phone number'
        elif len(phone_number) != 14:
            data['phone_number_error'] = 'Please enter the correct phone number format like 00923xxxxxxxxx'
        elif find_user(phone_number) != (None, None):
            print(find_user(phone_number))
            data['phone_number_error'] = 'Phone number already exists'
        elif not email:
            data['email_error'] = 'Please enter an email address'
        # Add email format validation using regular expression here
        elif find_user(email) != (None, None):
            data['email_error'] = 'Email already exists'
        elif len(password) < 8:
            data['password_error'] = 'Please enter a password with at least 8 characters'
        elif password != confirm_password:
            data['confirm_password_error'] = "Passwords don't match"
        else:
            email_otp = random.randint(100000, 999999)
            phone_otp = random.randint(100000, 999999)
            try:
                customer = Customer(
                    first_name=first_name.upper(),
                    last_name=last_name.upper(),
                    password=make_password(password),
                    email=email,
                    phone_number=phone_number,
                    email_otp=email_otp,
                    phone_otp=phone_otp,
                )
                customer.save()
                create_customer_activity(customer, 'customer')
            except IntegrityError:  # Catch specific IntegrityError for uniqueness constraint violation
                data['error'] = 'Sorry! Profile was not created due to a database error'
                return render(request, 'Registration.html', data)
                # All validations passed, proceed with OTP generation or further steps
            return redirect('accounts:login_page')

        # If any validation failed, render the signup form with error messages
        return render(request, 'registration.html', data)


"""
##==============================##
##    Login Page View Class     ##
##==============================##

"""


class Login(View):
    # Get Function for Login Class
    def get(self, request):
        return render(request, 'login.html')

    # Post Function for Login Class
    def post(self, request):
        data = {}
        input_data = request.POST.get("input_data")
        password = request.POST.get('password')

        # Check if the input_data is a phone number or email
        # Find the user and their profile type
        user, profile_type = find_user(input_data)

        if user and check_password(password, user.password):
            if profile_type == 'user':
                # Log user login with the profile type
                log_user_login(user, profile_type)
                request.session['profile_email'] = user.email
                request.session['profile_type'] = profile_type
                return redirect('dashboard:dashboard')
            elif profile_type == 'customer':
                # Log customer login with the profile type
                log_customer_login(user, profile_type)
                request.session['profile_email'] = user.email
                request.session['profile_type'] = profile_type
            elif profile_type == 'vendor':
                # Log vendor login with the profile type
                log_vendor_login(user, profile_type)
                request.session['profile_email'] = user.email
                request.session['profile_type'] = profile_type
            return redirect('frontend:landing_page')
        error_message = 'Incorrect email/phone or password'
        return render(request, 'login.html', {'error': error_message})


"""
##==========================##
##    Find User Function    ##
##==========================##

"""


def find_user(input_data):
    # Check if the input_data is a phone number or email for User, Customer, or Vendor
    models = [(User, 'user'), (Customer, 'customer'), (Vendor, 'vendor')]
    for model in models:
        profile = model[0].objects.filter(phone_number=input_data).first() or \
            model[0].objects.filter(email=input_data).first()
        if profile:
            return profile, model[1]
    return None, None


"""
##===============================##
##    Logout Page View Class     ##
##===============================##

"""


class Logout(View):
    # Get Function For Logout Class
    def get(self, request):
        profile_type = request.session.get('profile_type')
        profile_email = request.session.get('profile_email')
        if profile_type == 'user':
            profile = User.objects.filter(email=profile_email).first()
            log_user_logout(profile, profile_type)
        elif profile_type == 'customer':
            profile = Customer.objects.filter(email=profile_email).first()
            log_customer_logout(profile, profile_type)
        elif profile_type == 'vendor':
            profile = Vendor.objects.filter(email=profile_email).first()
            log_vendor_logout(profile, profile_type)
        request.session.clear()
        return render(request, 'index.html')

    # Post Function For Logut Class
    def post(self, request):
        return render(request, 'index.html')


"""
##=============================##
##    OTP  Page View Class     ##
##=============================##

"""


class OTP_Verification(View):
    # Get Function for OTP
    def get(self, request):
        return render(request, 'otp_verification.html')

    # Post Function for OTP
    def post(self, request):
        otp = request.POST.get('otp')
        otp1 = request.POST.get('otp1')
        otp2 = request.POST.get('otp2')
        otp3 = request.POST.get('otp3')
        otp4 = request.POST.get('otp4')
        otp5 = request.POST.get('otp5')
        otp6 = request.POST.get('otp6')
        confirm_otp = str(otp1) + str(otp2) + str(otp3) + \
            str(otp4) + str(otp5) + str(otp6)
        print(type(confirm_otp), confirm_otp)
        print(type(otp), otp)
        if str(confirm_otp) == str(otp):
            return redirect('login page')
        else:
            data = {
                'error': 'Invalid OTP',
                'otp': otp,
            }
            return render(request, 'otp_verification.html', data)


def send_otp(phone_number):
    otp = random.randint(100000, 999999)
    message = f'Your OTP for Kainat Plastic Industry App is {otp} For any issues, Contact us at 0322-4704244 or www.kainat.com.pk/contact'
    # Get the current date and time
    now = datetime.now()

    # Extract the current hour and minute
    hour = now.hour
    minute = now.minute + 1
    # Remove Prefix from Phone Number
    prefix_removed = phone_number[1:]
    # Send the message
    phone_number = '+92'+phone_number
    message_sent = wt.sendwhatmsg(phone_number, message, hour, minute)
    print(otp)
    return otp


def otp_verification(first_name, last_name, phone_number, email, password, confirm_password):
    pass


class Privacy_Policy(View):
    def get(self, request):
        return render(request, 'privacy_policy.html')


class Data_Deletion(View):
    def get(self, request):
        return render(request, 'data_deletion.html')
