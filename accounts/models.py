from django.db import models
from django.utils.translation import gettext_lazy as _

"""
##=============================##
##    Profile Model Class      ##
##=============================##

"""
class Profile(models.Model):
    first_name = models.CharField(_('First Name'), max_length=150)
    last_name = models.CharField(_('Last Name'), max_length=150)
    email = models.EmailField(_('Email'), unique=True)
    phone_number = models.CharField(_('Phone Number'), max_length=20, unique=True)
    password = models.CharField(_('Password'), max_length=150)
    bio = models.TextField(_('Bio'), blank=True)
    profile_picture = models.ImageField(_('Profile Picture'), upload_to='profile_pictures/', blank=True, null=True)
    date_of_birth = models.DateField(_('Date of Birth'), blank=True, null=True)
    address = models.TextField(_('Address'), blank=True)
    city = models.CharField(_('City'), max_length=100, blank=True)
    country = models.CharField(_('Country'), max_length=100, blank=True)
    email_otp = models.CharField(_('Email OTP'), max_length=100)
    phone_otp = models.CharField(_('Phone Number OTP'), max_length=100)
    email_verified = models.BooleanField(_("Email Verified"), default=False)
    phone_verified = models.BooleanField(_('Phone Verified'), default=False)
    is_delete = models.BooleanField(_('Is Delete'), default=False)
  

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
        abstract = True


    def __str__(self):
        return f'{self.first_name} {self.last_name}'



"""
##================================##
##  User Profile Model Class      ##
##================================##

"""
class User(Profile):
    GROUP_CHOICES = (
        ('admin', 'Admin'),
        ('sale', 'Sale'),
        ('purchase', 'Purchase'),
        ('account', 'Account'),
    )
    group = models.CharField(_('Group'), max_length=20, choices=GROUP_CHOICES)


"""
##===========================##
## Customer Model Class      ##
##===========================##

"""
class Customer(Profile):
    company = models.CharField(_('Company Name'), max_length=100, blank=False)
    company_phone_number = models.CharField(_('Company Phone Number'), max_length=14)
    company_phone_number_1 = models.CharField(_('Company Phone Number 1'), max_length=14)
    opening_balance = models.DecimalField(_('Opening Balance'), max_digits=10, decimal_places=2, default=0)


"""
##==========================##
##  Vendor Model Class      ##
##==========================##

"""
class Vendor(Profile):
    company = models.CharField(_('Company Name'), max_length=100, blank=False)
    company_phone_number = models.CharField(_('Company Phone Number'), max_length=14)
    company_phone_number_1 = models.CharField(_('Company Phone Number 1'), max_length=14)
    opening_balance = models.DecimalField(_('Opening Balance'), max_digits=10, decimal_places=2, default=0)



"""
##============================##
##  Activity Model Class      ##
##============================##

"""
class Activity(models.Model):
    PROFILE_TYPES = (
        ('user', 'User'),
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
    )
    profile_type = models.CharField(max_length=20, choices=PROFILE_TYPES)
    activity = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    # Use a GenericForeignKey to link to different profile types
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    customer_profile = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    vendor_profile = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _("Activity")
        verbose_name_plural = _("Activities")

    def __str__(self):
        return f"{self.profile_type} Activity - {self.activity} - {self.timestamp}"