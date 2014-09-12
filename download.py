from scp_celery.tasks import download
from local_settings import num_of_computer

for i in range(num_of_computer):
	download.delay("http://140.116.21.177/NCKUMath201409.ova")
