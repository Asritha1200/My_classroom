from  . import views
from django.urls import path, include

urlpatterns=[
 
    path("",views.index,name="index"),
    path("index/",views.index,name="index"),
    
    path("student/time_table",views.time_table,name="timetable"),
    path("student/to_do",views.to_do,name="to_do"),
    path("student/intatt",views.intattd,name="intatt"),
    path("student/profile",views.profile,name="profile"),
    path("signup/",views.signup,name="signup"),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('accounts/login/',views.login,name="login"),
    path('accounts/login/',views.logout,name="logout"),
    path('', views.home, name='home'),
    

] 