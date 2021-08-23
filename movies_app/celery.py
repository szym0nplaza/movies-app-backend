import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movies_app_config.settings')

app = Celery('movies_app', broker='redis://redis:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
