# +++++++++++ DJANGO +++++++++++
import os
import sys

## assuming your Django settings file is at '/home/my_username/projects/my_project/settings.py'
path = '/home/awwester/steps'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'stepsofatraveler.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()