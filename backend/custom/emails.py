import functools
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from accounts.models import CustomUser


def enable_mail(func:callable):
    '''Wraps a "mail" function to enable the sending of mails'''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if settings.SEND_MAIL:
            return func(*args, **kwargs)
        return None
    return wrapper
