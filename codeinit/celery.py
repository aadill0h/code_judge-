from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeinit.settings')

app = Celery('codeinit')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Optional: this is needed to make the Celery app work well with Django
# You can also make a shared Celery app that can be used in other places
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
