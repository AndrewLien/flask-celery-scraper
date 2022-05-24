import requests
import datetime
import logging
import sys
r = requests.get('https://pypistats.org/top')
data = r.text

filename = __file__.split('/')[-1].split('.')[0]
print(filename)

now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
print(now)

logging.basicConfig(
    format='%(asctime)s|%(name)s:%(lineno)s|%(levelname)s|%(message)s',
    level=logging.DEBUG,
    stream=sys.stdout,
)

logger = logging.getLogger('test.py')

logger.debug('this is level debug')
logger.info('this is level info')

with open('project/output/' + filename + '_' + now, 'w+') as f:
    f.write(data)
