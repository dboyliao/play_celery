from scp_celery.tasks import download
from local_settings import num_of_computer
from local_settings import TARGET_URL

for i in range(num_of_computer):
	download.delay(TARGET_URL)
