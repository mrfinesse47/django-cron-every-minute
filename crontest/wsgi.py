"""
WSGI config for crontest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from my_app.scheduler import start_jobs

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crontest.settings')

application = get_wsgi_application()

start_jobs()#load the cron job here or else it registers twice
