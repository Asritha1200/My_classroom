from  . import views
from django.urls import path, include

urlpatterns=[
 
    path("",views.index,name="index"),
    path("index/",views.index,name="index"),
    
    path("student/time_table",views.timeTable,name="timetable"),
    path("student/to_do",views.toDo,name="to_do"),
    path("student/intatt",views.intattd,name="intatt"),
    path("student/profile",views.profile,name="profile"),
    path("signup/",views.signup,name="signup"),
   
    path('accounts/login/',views.login,name="login"),
    path('accounts/logout/',views.logout,name="logout"),
    path('', views.home, name='home'),
    

] 