"""
WSGI config for API_Server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import sys
import os
import json
from django.core.wsgi import get_wsgi_application

# .config_secret setting
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, '.config_secret')
CONFIG_SECRET_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')
config_secret_common = (json.loads(open(CONFIG_SECRET_COMMON_FILE).read()))['django']

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'API_Server.settings')
sys.path.append(config_secret_common['wsgi']['project_path'])

application = get_wsgi_application()
