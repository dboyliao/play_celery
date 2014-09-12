from __future__ import absolute_import
from celery import Celery
from local_settings import BROCKER_URL, BACKEND_URL

app = Celery(
	'scp_celery',
    broker=BROCKER_URL,
    backend=BACKEND_URL,
    include=['scp_celery.tasks']
)

if __name__ == '__main__':
    app.start()
