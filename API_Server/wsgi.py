"""
WSGI config for API_Server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'API_Server.settings')
# sys.path.append('C:/Apache24/htdocs')

application = get_wsgi_application()
