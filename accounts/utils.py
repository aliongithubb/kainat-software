from .models import *

# User related activities

def create_user_activity(user, profile_type):
    activity = f"{user.phone_number} created"
    Activity.objects.create(user_profile=user, activity=activity, profile_type=profile_type)

def update_user_activity(user, profile_type):
    activity = f"{user.phone_number} updated"
    Activity.objects.create(user_profile=user, activity=activity, profile_type=profile_type)

def delete_user_activity(user, profile_type):
    activity = f"{user.phone_number} deleted"
    Activity.objects.create(user_profile=user, activity=activity, profile_type=profile_type)

def log_user_login(user, profile_type):
    activity = f"{user.phone_number} logged in"
    Activity.objects.create(user_profile=user, activity=activity, profile_type=profile_type)

def log_user_logout(user, profile_type):
    activity = f"{user.phone_number} logged out"
    Activity.objects.create(user_profile=user, activity=activity, profile_type=profile_type)

# Customer related activities

def create_customer_activity(customer, profile_type):
    activity = f"{customer.phone_number} created"
    Activity.objects.create(customer_profile=customer, activity=activity, profile_type=profile_type)

def update_customer_activity(customer, profile_type):
    activity = f"{customer.phone_number} updated"
    Activity.objects.create(customer_profile=customer, activity=activity, profile_type=profile_type)

def delete_customer_activity(customer, profile_type):
    activity = f"{customer.phone_number} deleted"
    Activity.objects.create(customer_profile=customer, activity=activity, profile_type=profile_type)

def log_customer_login(customer, profile_type):
    activity = f"{customer.phone_number} logged in"
    Activity.objects.create(customer_profile=customer, activity=activity, profile_type=profile_type)

def log_customer_logout(customer, profile_type):
    activity = f"{customer.phone_number} logged out"
    Activity.objects.create(customer_profile=customer, activity=activity, profile_type=profile_type)

# Vendor related activities

def create_vendor_activity(vendor, profile_type):
    activity = f"{vendor.phone_number} created"
    Activity.objects.create(vendor_profile=vendor, activity=activity, profile_type=profile_type)

def update_vendor_activity(vendor, profile_type):
    activity = f"{vendor.phone_number} updated"
    Activity.objects.create(vendor_profile=vendor, activity=activity, profile_type=profile_type)

def delete_vendor_activity(vendor, profile_type):
    activity = f"{vendor.phone_number} deleted"
    Activity.objects.create(vendor_profile=vendor, activity=activity, profile_type=profile_type)

def log_vendor_login(vendor, profile_type):
    activity = f"{vendor.phone_number} logged in"
    Activity.objects.create(vendor_profile=vendor, activity=activity, profile_type=profile_type)

def log_vendor_logout(vendor, profile_type):
    activity = f"{vendor.phone_number} logged out"
    Activity.objects.create(vendor_profile=vendor, activity=activity, profile_type=profile_type)
