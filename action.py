from source.body_crawler import *
from source.save_data import *
from source.custom_data import *

import yaml
with open("config/config.yaml", 'r') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as error:
        print(error)

if 'extension' in data.get('HARD','-1'):
    a=Extensions(data['HARD']['extension'])
else:
    a=Extensions()

b=create_broswer('chromdrive/chromedriver',a)   
if 'url' in data.get('HARD','-1'):
    url = data['HARD']['url']

c=Open_web(b,url)

# list_key=data['LOOP']
# print(list_key)
for i in data['LOOP'].keys():
    print(i)
# number=int(data['LOOP'][0].get('number'))
# start=int(data['LOOP'][1].get('start'))
# for i in range(start,number+start):
    
    
    

d=Close_web(b)