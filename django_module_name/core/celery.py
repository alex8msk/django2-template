from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.dev')

app = Celery('{{ files.1 }}_celery')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
