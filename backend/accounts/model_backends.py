from django.contrib.auth.backends import ModelBackend
from django.http import HttpRequest
from django.db.models import Q
from accounts.models import CustomUser as User


class UserEmailBackend(ModelBackend):
    '''
    Custom User Authentication Method

    Both "username" and "email" are accepted
    '''

    def authenticate(self, request:HttpRequest, username:str|None=None, password:str|None=None, **kwargs):
        '''Authentication Method'''

        # Try to do the query:
        try:
            user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except User.DoesNotExist:
            User().set_password(password)
            return
        except User.MultipleObjectsReturned:
            user = User.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by('id').first()

        # Auth and return user:
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
