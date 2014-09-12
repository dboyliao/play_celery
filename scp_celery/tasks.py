from __future__ import absolute_import
from scp_celery.celery import app

import os

@app.task
def dowload(path):
	cmd = "wget " + TARGET_URL
	os.system(cmd)
