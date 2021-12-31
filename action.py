from source.body_crawler import *
from source.save_data import *
from source.custom_data import *

import yaml
with open("config/new.yaml", 'r') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as error:
        print(error)

if 'extension' in data.get('HARD','-1'):
    a=Extensions(data['HARD']['extension'])
else:
    a=Extensions()

b=create_browser('chromdrive/chromedriver',a)   
if 'url' in data.get('HARD','-1'):
    url = data['HARD']['url']

c=Open_web(b,url)
number=int(data['LOOP'][0].get('number',None))
start=int(data['LOOP'][1].get('start',None))
num=start
data_save=[]
if number is None:
    print("bạn vui lòng nhập số lượng cần loop")
else:
    if start is None:
        print("bạn vui lòng nhập số bắt đầu")
    else:
        for i in range(start,number+start):
            action_dict={}
            long=len(data['LOOP'])
            if long != 3:
                print('long',long)
            else:
                list_key=data['LOOP'][2].keys()
                for i in list_key:
                    if 'xpath' in i:
                        list_index = i.split('_')
                        action = list_index[1]
                        if action is 'click':
                            xpath=data['LOOP'][2].get(i,None)
                            if xpath != None:
                                if 'start' in xpath:
                                    track_xpath = xpath.split("start")
                                    path=track_xpath[0]+str(num)+track_xpath[1]
                                    Click_button(path)
                        else:
                            xpath=data['LOOP'][2].get(i,None)
                            if xpath is not None:
                                if 'start' in xpath:
                                    track_xpath = xpath.split('start')
                                    path=track_xpath[0]+str(num)+track_xpath[1]   
                                    variable=Find_xpath(b,path)
                                    type=data['LOOP'][2].get(i+1,None)
                                    if 'type' in type:
                                        val=get_data(variable,type=type) 
                                    action_dict[action]=val  
                                else:
                                    path=xpath
                                    variable=Find_xpath(b,path)
                                    if 'type' in type:
                                        val=get_data(variable,type=type)
                                    action_dict[action]=val             
            num+=1
            print(action_dict)

# i = data['SAVE'].get('type',None)
# if i == None:
# df = pd.DataFrame(data,columns = [])  
    
    
    

d=Close_web(b)