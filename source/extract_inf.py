from source.body_crawler import *
from source.save_data import *
from source.custom_data import *
import yaml

# hàm read config
def load_configure(path):
    with open(path, 'r') as stream:
        data=[]
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as error:
            print(error)
    return data
# hàm rút ra extension
def extract_extension(data):
    extension=Extensions()
    for i in range(len(data['HARD'])):
        if data['HARD'][i].get('extension',None) != None:
            extension = data['HARD'][i]['extension']
    return extension
# ham lay url
def track_url(data):
    url=None
    for i in range(len(data['HARD'])):
        if data['HARD'][i].get('url',None) != None:
            url = data['HARD'][i]['url']
    return url
# ham lay start,number
def track_start(data):
    start=0
    for i in range(len(data['HARD'])):
        if data['HARD'][i].get('start',0) != 0:
            start = data['HARD'][i]['start']
    return start
def track_number(data):
    number=0
    for i in range(len(data['HARD'])):
        if data['HARD'][i].get('number',0) != 0:
            number = data['HARD'][i]['number']
    return number
# ham lay ra loop
def Create_loop(data):
    start=int(0)
    number=int(0)
    for i in data['HARD']:
        
        if start == 0:
            start=int(i.get('start','0'))
        if number == 0:
            number=int(i.get('number','0'))
    return start,number

# hàm tách ra xpath

def track_xpath(xpath):
    for i in ['xpath','class','id']:   
        if i in xpath:
            track_xpath=xpath.split('_')
            return track_xpath
    
# hàm lấy dữ liệu trong xpath
def track_inf_xpath(track_xpath):
    if len(track_xpath) == 3:
        kind_of_find = track_xpath[0]
        action = track_xpath[1]
        type = track_xpath[2]
    else:
        kind_of_find = track_xpath[0]
        action = track_xpath[1]  
        type = None  
    return kind_of_find,action,type
# ham lay path_value trong xpath

    
# hàm lấy vị trí element
def track_inf_elenment(data):
    for i in data['LOOP']:
        if i in ['xpath','class','id']:
            local_elenment = data['LOOP'].get(i,None)
    return local_elenment
            

# hàm lấy ra columns trong file config    
def create_columns(data):
    columns=[]
    for i in data:
        #print(i)
        for key in i.keys():
            #print(key)
            result=track_xpath(key)
            if result != None and 'click' not in result:
                #print(result)
                columns.append(result[1])
    return columns

# ham lay ra type save trong file configs
def track_save(data):
    type_save = data['SAVE'][1].get('type','csv')
    path_save="save/"+data['SAVE'][0].get('name','data')+"."+type_save
    return type_save,path_save

# ham load data
def Load_data(start,number,browser,data,data_save):
    for i in range(start,number):
        cache_dict={}
        for i in range(len(data['LOOP'])):
            variable=data['LOOP'][i]
            for value in variable.values():
                value = value
            for key in variable.keys():    
                track_xpath_value = track_xpath(key)
                kind_of_find,action,type_xpath=track_inf_xpath(track_xpath_value)
                if action == 'click':
                    results=Find_xpath(browser,value)
                    Click_button(results)
                else:
                    if kind_of_find=='xpaths':
                        results=Find_xpath(browser,value,True)
                        var=get_data(results,True,type=type_xpath)
                        cache_dict[action]=var
                    else:
                        results=Find_xpath(browser,value,False)
                        var=get_data(results,type=type_xpath)
                        cache_dict[action]=var
        data_save.append(cache_dict)
    return data_save