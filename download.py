from scp_celery.tasks import download
from local_settings import num_of_computer, TARGET_URL

for i in range(num_of_computer):
	download.delay(TARGET_URL)
