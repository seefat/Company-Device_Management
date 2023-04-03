from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Company, Employee, Device, CheckIn, CheckOut, DeviceLog

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your first name.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your last name.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'contact_info']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone_number']

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['device_type', 'serial_number']

class CheckOutForm(forms.ModelForm):
    class Meta:
        model = CheckOut
        fields = ['employee', 'device', 'checkout_date', 'expected_return_date']

class CheckInForm(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = ['employee', 'device', 'checkin_date', 'condition', 'notes']

class DeviceLogForm(forms.ModelForm):
    class Meta:
        model = DeviceLog
        fields = ['condition', 'notes']
