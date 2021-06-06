from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,"index.html")




def optout(request):
    return redirect("http://stackoverflow.com/")