from __future__ import absolute_import
from scp_celery.celery import app

import os

@app.task
def download(path):
    cmd = "wget " + path
    os.system(cmd)
