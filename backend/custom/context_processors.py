from django.conf import settings
from django.http import HttpRequest


def server_descriptors(request:HttpRequest|None):
    '''Add server related variables to all project template contexts'''
    return {
        'deployment_stage': settings.DEPLOYMENT_STAGE,
        'private_ip': settings.PRIVATE_SERVER_IP,
        'http_port': settings.HTTP_PORT,
        'https_port': settings.HTTPS_PORT,
        'domain_url': settings.DOMAIN_URL,
        'domain_url_secure': settings.DOMAIN_URL_SECURE,
    }
