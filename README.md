# My Classroom
My classroom deals with the maintenance of the student’s information,attendance, internal marks. It displays the student’s time-table, tasks and the upcoming events.
There are two types of users: the admin, the students.
The admin can add/modify/delete students’ information, attendance, internal marks, time-table, tasks and events.

## Installation

Python and Django need to be installed

```bash
pip install django
```

## Usage

Go to the My_classroom folder and run

```bash
python manage.py runserver
```

Then go to the browser and enter the url **http://127.0.0.1:8000/**


## Login

The students can login using the usn and the password

Example usernames and password:
student- '95',Password-'asri123'


You can access the django admin page at **http://127.0.0.1:8000/admin**
Also a new admin user can be created using

```bash
python manage.py createsuperuser
```

## Users

New students can be added through the admin page. 

The admin page is used to modify all tables such as Students, Teachers, Departments, Courses, Classes,Attendance,Marks etc

