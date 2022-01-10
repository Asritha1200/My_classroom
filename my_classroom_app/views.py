from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import branch,sem,classroom,student,prof,time_table,to_do,events,internals,attendance,class_courses,courses


# Create your views here.

@login_required()
def index(request):
    
        event=events.objects.all()
        return render(request,"index.html",{'events':event})




@login_required()

def time_table(request,student_id):
    stud=student.objects.get(usn=student_id)
    return render(request,"timetable.html")

 

def profile(request,student_id):
    stud = student.objects.get(usn=student_id)
    

    return render(request,"profile.html",{'student':stud})

def intattd(request,student_id,sem_id):
    stud = student.objects.get(usn=student_id)
    cou=courses.objects.get(sem=sem_id)
    
    return render(request,"internals&attendance.html")


def to_do(request,classroom_id,student_id):
    stud=student.objects.get(usn=student_id)
    tasks=to_do.objects.get(class_id=classroom_id)
    return render(request,"to_do.html",{'tasks':tasks,'student':stud})



