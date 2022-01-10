from django.contrib import admin
from .models import branch, sem,classroom,internals,courses,class_courses,student,attendance,internals,to_do,events,time_table,prof


admin.site.register(branch)
admin.site.register(sem)
admin.site.register(classroom)
admin.site.register(student)
admin.site.register(attendance)
admin.site.register(internals)
admin.site.register(time_table)
admin.site.register(to_do)
admin.site.register(courses)
admin.site.register(class_courses)
admin.site.register(prof)
admin.site.register(events)

# Register your models here.

      
    