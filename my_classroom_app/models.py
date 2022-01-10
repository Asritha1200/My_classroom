from django.db import models
from django.db.models.aggregates import Max

# Create your models here.
SEMESTER_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
)
time_slots = (

    ('8:30 - 9:30', '8:30 - 9:30'),
    ('9:30 - 10:30', '9:30 - 10:30'),
    ('11:00 - 11:50', '11:00 - 11:50'),
    ('11:50 - 12:40', '11:50 - 12:40'),
    ('12:40 - 1:30', '12:40 - 1:30'),
    ('2:30 - 3:30', '2:30 - 3:30'),
    ('3:30 - 4:30', '3:30 - 4:30'),
    ('4:30 - 5:30', '4:30 - 5:30'),
)

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)
class branch(models.Model):
     branch_id=models.CharField(max_length=50,primary_key=True)
     branch=models.CharField(max_length=100,default='default')
     
     def __str__(self):
        return self.branch_id

class sem(models.Model):
   sem=models.CharField(primary_key=True,max_length=1,choices=SEMESTER_CHOICES)

   def __str__(self):
        return self.sem 

class classroom(models.Model):
    class_id=models.CharField(primary_key=True,max_length=10 )
    branch_id=models.ForeignKey(branch,on_delete=models.CASCADE)
    section=models.CharField(max_length=5)
    sem=models.ForeignKey(sem,on_delete=models.CASCADE)
  
    def __str__(self):
        return self.class_id
        #d = branch.objects.get(branch_id=self.branch_id)
        #return '%s : %s %s' % (d.branch, self.sem,self.section)

    

class student(models.Model):
    usn = models.CharField(max_length=10,primary_key=True)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    
    class_id = models.ForeignKey(classroom,on_delete=models.CASCADE)
    gender = models.CharField(max_length = 10)
    phoneno = models.CharField(max_length = 12)
    email=models.EmailField(max_length = 254)
    DOB=models.DateField()

    def __str__(self):
        return self.usn

class courses(models.Model):
    course_name=models.CharField(max_length=150)
    course_id = models.CharField(primary_key=True,max_length=10 )
    branch_id=models.ForeignKey(branch,on_delete=models.CASCADE)
    sem=models.ForeignKey(sem,on_delete=models.CASCADE)
    is_elective=models.BooleanField(default=False)

    def __str__(self):
        return self.course_name 
    
#class student_courses(models.Model):
 #   usn = models.ForeignKey(student,on_delete=models.CASCADE)
  #  class_id = models.ForeignKey(classroom,on_delete=models.CASCADE)
   # course_id = models.IntegerField()
    #is_elected = models.BooleanField(default=False)
    
class prof(models.Model):
    prof_name = models.CharField(max_length=50)
    branch_id = models.ForeignKey(branch,on_delete=models.CASCADE)
    desig = models.CharField(max_length=50)
    prof_id = models.CharField(primary_key=True,max_length=10 )

    def __str__(self):
        return self.prof_name 

class class_courses(models.Model):
    class_id = models.ForeignKey(classroom,on_delete=models.CASCADE)
    course_id = models.ForeignKey(courses,on_delete=models.CASCADE)
    prof_id = models.ForeignKey(prof,on_delete=models.CASCADE)

    def __str__(self):
        class_id=self.class_id
        course_id=self.course_id
        prof_id=self.prof_id
        cr = classroom.objects.raw('Select * from myapp_class_courses where class_id=%s',[class_id])#cr = classroom.objects.get(class_id=self.class_id)
        co= classroom.objects.raw('Select * from myapp_class_courses where course_id=%s',[course_id])#co = courses.objects.get(course_id=self.course_id)
        pr=prof.objects.raw('Select * from myapp_class_courses where prof_id=%s',[prof_id])#pr = prof.objects.get(prof_id=self.prof_id) 
        return '%s : %s : %s' % (cr.class_id, co.course_name, pr.prof_nmae)



class attendance(models.Model):
    usn= models.ForeignKey(student,on_delete=models.CASCADE)
    course_id= models.ForeignKey(courses,on_delete=models.CASCADE)
    a1 = models.IntegerField(default=0)
    a2 = models.IntegerField(default=0)
    a3 = models.IntegerField(default=0)
    avg = models.FloatField(default=0.0)
    
    def __str__(self):

        usn=self.usn
        course_id=self.course_id
        sname= classroom.objects.raw('Select * from my_classroom_app_student where class_id=%s',[usn])#sname = student.objects.get(usn=self.usn)
        cname = classroom.objects.raw('Select * from my_classroom_app_courses where class_id=%s',[course_id])#cname = courses.objects.get(course_id=self.course_id)
        return '%s : %s' % (sname.user_name, cname.course_name)

class internals(models.Model):
    usn = models.ForeignKey(student,on_delete=models.CASCADE)
    course_id = models.ForeignKey(courses,on_delete=models.CASCADE)
    ia1 = models.IntegerField(default=0)
    ia2 = models.IntegerField(default=0)
    ia3 = models.IntegerField(default=0)
    final_ia= models.FloatField(default=0.0)


    def __str__(self):
        usn=self.usn
        course_id=self.course_id
        sname= classroom.objects.raw('Select * from my_classroom_app_student where class_id=%s',[usn])#sname = student.objects.get(usn=self.usn)
        cname= classroom.objects.raw('Select * from my_classroom_app_courses where class_id=%s',[course_id])#cname = courses.objects.get(course_id=self.course_id)
        return '%s : %s' % (sname.user_name, cname.course_name)
    
class time_table(models.Model):
    assign= models.ForeignKey(class_courses,on_delete=models.CASCADE)
    day=models.CharField(max_length=20,choices=DAYS_OF_WEEK)
    time = models.TimeField(choices=time_slots)

   



class to_do(models.Model):
    class_id = models.ForeignKey(classroom,on_delete=models.CASCADE)
    text = models.TextField()
    due_date = models.DateField()
    
    def __str__(self):
        return self.class_id
        #cr = classroom.objects.get(class_id=self.class_id)
        #return '%s' % (cr.class_id)

class events(models.Model):
    date = models.DateTimeField()
    text = models.TextField()
    
   
    


