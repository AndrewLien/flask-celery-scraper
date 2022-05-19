import requests
import datetime

r = requests.get('https://pypistats.org/top')
data = r.text

filename = __file__.split('/')[-1].split('.')[0]
print(filename)

now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
print(now)

with open('project/output/' + filename + '_' + now, 'w+') as f:
    f.write(data)
