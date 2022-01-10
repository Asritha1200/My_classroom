from django.urls import path
from  . import views
urlpatterns=[
 
    path("",views.index,name="index"),

    
    path("student/slug:<student_id>/slug:<classroom_id>/time_table",views.time_table,name="timetable"),
    path("student/slug:<student_id>/slug:<classroom_id>/to_do",views.to_do,name="to_do"),
    path("student/slug:<student_id>/slug:<sem_id>/intatt",views.intattd,name="intatt"),
    path("student/slug:<student_id>/profile",views.profile,name="profile"),
    

] 