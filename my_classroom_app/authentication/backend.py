from django.contrib.auth.hashers import check_password 

from django.contrib.auth.models import User

from my_classroom_app.models import student


class StudentBackend:

    # Create an authentication method
    # This is called by the standard Django login procedure
    def authenticate(self, usn=None, password=None):

        try:
            # Try to find a user matching your username
            user = student.objects.get(usn=usn)
            print(password)
            print(user.password)
            #  Check the password is the reverse of the username
            if (password == user.password):
                # Yes? return the Django user object
                return user
            else:
                print('Incorrect Password')
                # No? return None - triggers default login failed
                return None
        except student.DoesNotExist:
            print('User does not exist')
            # No user was found, return None - triggers default login failed
            return None

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, usn):
        try:
            return student.objects.get(usn=usn)
        except student.DoesNotExist:
            return None