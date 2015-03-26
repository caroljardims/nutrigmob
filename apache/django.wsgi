import os
import sys

path = '/home/bruno/django-projects/nutri'
if path not in sys.path:
	sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'nutri.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
