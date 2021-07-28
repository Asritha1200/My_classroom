from django.shortcuts import render,redirect


# Create your views here.


def index(request):
    return render(request,"index.html")


def time_table(request):
    return render(request,"timetable.html")

def login(request):
    return render(request,"login.html")

def profile(request):
    return render(request,"profile.html")

def intattd(request):
    return render(request,"internals&attendance.html")


def to_do(request):
    return render(request,"to_do.html")



