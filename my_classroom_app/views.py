
from django.contrib import auth
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from my_classroom_app.authentication.backend import StudentBackend
from my_classroom_app.models import student
from my_classroom_app.forms.student_form import StudentSignInForm, StudentSignUpForm

from .models import branch,sem,classroom,student,prof,time_table,to_do,events,internals,attendance,class_courses,courses


# Create your views here.
def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })
def signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user,backend='my_classroom_app.authentication.backend.StudentBackend')
            return redirect('/')
    else:
        form = StudentSignUpForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

def login(request):
    if request.method=='POST':
        form = StudentSignInForm(request.POST)
        if form.is_valid():
            usn_ma = form.cleaned_data['usn']
            password_ma = form.cleaned_data['password']
            user = auth.authenticate(
                usn=usn_ma,password=password_ma)
            if(user):
                print("Authenticated")
                auth.login(request,user,backend='my_classroom_app.authentication.backend.StudentBackend')
                print('done')
                return redirect('/index')
            else:
                return redirect('/accounts/login')    
           
    else:
        form = StudentSignInForm(request.POST)
    return render(request,'registration/login.html',{'form':form})        

def logout(request):
    auth.logout(request)
    return redirect('/accounts/login')
    print("LOGOUT")

@login_required()
def index(request):
        current_user = request.user
        event=events.objects.all()
        return render(request,"index.html",{'events':event,'user':current_user})




@login_required()

def time_table(request):
    current_user = request.user
    return render(request,"timetable.html",{})

 

def profile(request):
    stud = student.objects.get(usn=student_id)
    

    return render(request,"profile.html",{'student':stud})

def intattd(request):
    
    
    return render(request,"internals&attendance.html")


def to_do(request):
    stud=student.objects.get(usn=student_id)
    tasks=to_do.objects.get(class_id=classroom_id)
    return render(request,"to_do.html",{'tasks':tasks,'student':stud})

@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'

