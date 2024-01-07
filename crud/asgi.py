"""
ASGI(Asynchronous Server Gateway Interface) config for crud project.----to hangle HTTP requests

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os #module imported from django.core.asgi

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud.settings')#django_se... set var to crus.settings
                                                                    #to know which setting module to use

application = get_asgi_application()#method to retrieve the ASGI application
