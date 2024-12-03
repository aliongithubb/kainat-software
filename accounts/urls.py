from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', Login.as_view(), name='login_page'),
    path('registration/', Registration.as_view(), name='registration_page'),
    path('otp_verification/', OTP_Verification.as_view(), name='otp_verification'),
    path('logout/', Logout.as_view(), name='logout'),
    
    # path('privacy_policy/', Privacy_Policy.as_view(), name='privacy_policy' ),
    # path('data_deletion/', Data_Deletion.as_view(), name='data_deletion' ),

  ]