from source.body_crawler import *
from source.save_data import *
from source.custom_data import *

import yaml
with open("config/new.yaml", 'r') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as error:
        print(error)
        

"""form run
version 1 : 1 loop
configure.yaml have
HARD:
url
extension
scroll
LOOP:
number:
start:
xpath_?
SAVE:
name:
param:default
type:csv

run:
load HARD to open website
load SAVE to create path_save name data
before load LOOP
data=[]
columns=[?]
begin LOOP
for i in range(start,number) if have this
for i in range(len(?)):
    name_dict= ...
    name_dict[?]=val(?)
    data.append(name_dict)
df=pd.DataFrame(data,columns=columns)
write_type(path_save,df)


command line to run : python system.py
"""


