from django.db import models

# Create your models here.
class classroom(models.Model):
    class_id=models.CharField(primary_key=True,max_length=10 )
    branch=models.CharField(max_length=50)
    section=models.CharField(max_length=5)
    sem=models.IntegerField()


class student(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    usn = models.CharField(max_length=1,primary_key=True)
    class_id = models.ForeignKey(classroom,on_delete=models.CASCADE)

class attendance(models.Model):
    usn= models.ForeignKey(student,on_delete=models.CASCADE)
    cousre_id= models.CharField(max_length=50)
    course= models.CharField(max_length=50)
    status= models.IntegerField()


    
class internals(models.Model):
    usn = models.ForeignKey(student,on_delete=models.CASCADE)
    course = models.CharField(max_length=20)
    course_id = models.IntegerField()
    a1 = models.IntegerField()
    a2 = models.IntegerField()
    a3 = models.IntegerField()
    avg = models.FloatField()
    
class time_table(models.Model):
    class_id = models.ForeignKey(classroom,on_delete=models.CASCADE)
    course_id = models.IntegerField()
    time = models.TimeField()


class to_do(models.Model):
    class_id = models.ForeignKey(classroom,on_delete=models.CASCADE)
    text = models.TextField()
    due_date = models.DateField()

class courses(models.Model):
    course_name=models.CharField(max_length=20)
    course_id = models.IntegerField()
    branch=models.CharField(max_length=20)
    sem=models.CharField(max_length=20)
    is_elective=models.BooleanField(default=False)

class class_courses(models.Model):
    class_id = models.ForeignKey(classroom,on_delete=models.CASCADE)
    course_id = models.IntegerField()
    prof_id = models.IntegerField()

class student_courses(models.Model):
    usn = models.ForeignKey(student,on_delete=models.CASCADE)
    class_id = models.ForeignKey(classroom,on_delete=models.CASCADE)
    course_id = models.IntegerField()
    is_elected = models.BooleanField(default=False)

class prof(models.Model):
    prof_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    desig = models.CharField(max_length=50)
    prof_id = models.IntegerField()

class events(models.Model):
    date = models.DateTimeField()
    text = models.TextField()
    
    



