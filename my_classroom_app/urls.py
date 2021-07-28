from django.urls import path
from  . import views
urlpatterns=[
    path("",views.login,name="login"),
    path("index",views.index,name="index"),

    
    path("time_table",views.time_table,name="timetable"),
    path("to_do",views.to_do,name="to_do"),
    path("intatt",views.intattd,name="intatt"),
    path("profile",views.profile,name="profile"),


] 