# Generated by Django 5.0.1 on 2024-02-08 20:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=20, unique=True, verbose_name='Phone Number')),
                ('password', models.CharField(max_length=150, verbose_name='Password')),
                ('bio', models.TextField(blank=True, verbose_name='Bio')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/', verbose_name='Profile Picture')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('address', models.TextField(blank=True, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='City')),
                ('country', models.CharField(blank=True, max_length=100, verbose_name='Country')),
                ('email_otp', models.CharField(max_length=100, verbose_name='Email OTP')),
                ('phone_otp', models.CharField(max_length=100, verbose_name='Phone Number OTP')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email Verified')),
                ('phone_verified', models.BooleanField(default=False, verbose_name='Phone Verified')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Is Delete')),
                ('company', models.CharField(max_length=100, verbose_name='Company Name')),
                ('company_phone_number', models.CharField(max_length=14, verbose_name='Company Phone Number')),
                ('company_phone_number_1', models.CharField(max_length=14, verbose_name='Company Phone Number 1')),
                ('opening_balance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Opening Balance')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=20, unique=True, verbose_name='Phone Number')),
                ('password', models.CharField(max_length=150, verbose_name='Password')),
                ('bio', models.TextField(blank=True, verbose_name='Bio')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/', verbose_name='Profile Picture')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('address', models.TextField(blank=True, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='City')),
                ('country', models.CharField(blank=True, max_length=100, verbose_name='Country')),
                ('email_otp', models.CharField(max_length=100, verbose_name='Email OTP')),
                ('phone_otp', models.CharField(max_length=100, verbose_name='Phone Number OTP')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email Verified')),
                ('phone_verified', models.BooleanField(default=False, verbose_name='Phone Verified')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Is Delete')),
                ('group', models.CharField(choices=[('admin', 'Admin'), ('sale', 'Sale'), ('purchase', 'Purchase'), ('account', 'Account')], max_length=20, verbose_name='Group')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=20, unique=True, verbose_name='Phone Number')),
                ('password', models.CharField(max_length=150, verbose_name='Password')),
                ('bio', models.TextField(blank=True, verbose_name='Bio')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/', verbose_name='Profile Picture')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('address', models.TextField(blank=True, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='City')),
                ('country', models.CharField(blank=True, max_length=100, verbose_name='Country')),
                ('email_otp', models.CharField(max_length=100, verbose_name='Email OTP')),
                ('phone_otp', models.CharField(max_length=100, verbose_name='Phone Number OTP')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email Verified')),
                ('phone_verified', models.BooleanField(default=False, verbose_name='Phone Verified')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Is Delete')),
                ('company', models.CharField(max_length=100, verbose_name='Company Name')),
                ('company_phone_number', models.CharField(max_length=14, verbose_name='Company Phone Number')),
                ('company_phone_number_1', models.CharField(max_length=14, verbose_name='Company Phone Number 1')),
                ('opening_balance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Opening Balance')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='profileactivity',
            name='profile',
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_type', models.CharField(choices=[('user', 'User'), ('customer', 'Customer'), ('vendor', 'Vendor')], max_length=20)),
                ('activity', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('customer_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
                ('vendor_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.vendor')),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='ProfileActivity',
        ),
    ]
