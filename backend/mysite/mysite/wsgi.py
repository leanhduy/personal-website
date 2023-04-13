"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

from dotenv import load_dotenv
import os
from django.conf import settings

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.base")
load_dotenv(os.path.join(settings.BASE_DIR, ".env"))

application = get_wsgi_application()
