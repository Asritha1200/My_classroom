
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
from my_classroom_app.forms.student_form import StudentSignInForm, StudentSignUpForm
from datetime import *

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
        event=events.objects.raw("SELECT * FROM my_classroom_app_events")
        return render(request,"index.html",{'events':event,'user':current_user})




@login_required()

def timeTable(request):
    current_user = request.user
    ccs = class_courses.objects.raw("SELECT * FROM my_classroom_app_class_courses where class_id_id = %s",[str(current_user.class_id)])
    
    tts=[] 
    for cc in ccs:
        tts.append(time_table.objects.raw("SELECT * FROM my_classroom_app_time_table where assign_id = %s",[str(cc.id)]))
        # tts.append()  
    for tt in tts:
        for t in tt:
            print(t) 
    profs = {}  
    finaltt = []

    for tt in tts:
        profs[tt[0].assign.course_id] = tt[0].assign.prof_id
        for t in tt:
            finaltt.append(t)   

    return render(request,"timetable.html",{'time_tables':finaltt,'profs':profs})

 

def profile(request):
    stud = request.user
    

    return render(request,"profile.html",{'student':stud})

def intattd(request):
    internal_scores = internals.objects.raw("SELECT * from my_classroom_app_internals where usn_id = %s",[request.user.usn])
    print(str(internal_scores))
    att = attendance.objects.raw("SELECT * from my_classroom_app_attendance where usn_id = %s",[request.user.usn])
    for att_per in att:
        att_per.avg = (att_per.a1+att_per.a2+att_per.a3)/3
    for score in internal_scores:
        score.final_ia = (score.ia1+score.ia2+score.ia3)*30/150 
    return render(request,"internals&attendance.html",{'att':att,'scores':internal_scores})


def toDo(request):
    stud=student.objects.get(usn=request.user.usn)
    tasks=to_do.objects.raw("SELECT * from my_classroom_app_to_do where class_id_id = %s",[str(stud.class_id)])
    for task in tasks:
        if(task.due_date<date.today()):
            task.status = "Overdue"
        else:
            task.status = "Due"    
    return render(request,"to_do.html",{'stud':stud,'tasks':tasks})