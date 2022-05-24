import os
import psutil
import subprocess
import logging

from celery import Celery
import sys
import datetime

now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")

logger = logging.getLogger('celery-app.tasks')
fh = logging.FileHandler('project/logs/' + now + '.log')
logger.addHandler(fh)

@celery.task(name="create_task")
def create_task(scrapename):
    # exec(open('project/scrapes/' + scrapename).read())
    # files = psutil.Process().open_files()  # this only returns celery log files
    # with open('files.txt', 'w') as f:
    #     f.write(str(f))
    cmd = [sys.executable, 'project/scrapes/' + scrapename]

    p = subprocess.Popen(cmd, universal_newlines=True,
                         # stdout=log_file,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)  # TODO tweak
    stdout, _ = p.communicate()
    logger.log(logging.INFO, stdout)
    return True
