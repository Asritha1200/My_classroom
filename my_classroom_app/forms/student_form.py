from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.forms.forms import Form
from django.forms.widgets import EmailInput, PasswordInput

from my_classroom_app.models import student


class StudentSignUpForm(ModelForm):
    # username = forms.CharField(label='Your Name',max_length=100)
    # usn = forms.CharField(label='Your Roll Number',max_length=100)
    # password = forms.CharField(widget=PasswordInput)
    # email = forms.CharField(widget=EmailInput)
    # gender = forms.CharField(label='Male/Female/Other')
    # phone = forms.CharField(label='Your Phone Number')
    # dob = forms.DateField(label='Your DOB')
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    class Meta:
        model = student
        fields = ["user_name", "usn", "password", "email", "class_id", "gender","phoneno","DOB"]
class StudentSignInForm(Form):
    # username = forms.CharField(label='Your Name',max_length=100)
    # usn = forms.CharField(label='Your Roll Number',max_length=100)
    # password = forms.CharField(widget=PasswordInput)
    # email = forms.CharField(widget=EmailInput)
    # gender = forms.CharField(label='Male/Female/Other')
    # phone = forms.CharField(label='Your Phone Number')
    # dob = forms.DateField(label='Your DOB')
    usn = forms.CharField(label='Usn')
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    class Meta:
        model = student
        fields = ["usn", "password"]        