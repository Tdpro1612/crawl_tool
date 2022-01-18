from source.body_crawler import *
from source.save_data import *
from source.custom_data import *
import yaml
# HÀM RÚT DỮ LIỆU TỪ HARD

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
    display=False
    for i in range(len(data['HARD'])):
        if data['HARD'][i].get('extension',None) != None:
            display = data['HARD'][i]['extension']
    return display
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

# ham load scroll
def track_scroll(data):
    scroll=None
    for i in range(len(data['HARD'])):
        if data['HARD'][i].get('scroll',None) != None:
            scroll = data['HARD'][i]['scroll']
    return scroll
def scroll_page(browser,scroll):
    # ytb = "document.documentElement.scrollHeight"
    # jav_scrip_tw_fb = "document.body.scrollHeight"
    if scroll == 'ytb':
        pause = 3
        lastHeight = browser.execute_script("return document.documentElement.scrollHeight")
        i = 0
        browser.get_screenshot_as_file("logs/image/test01_1_"+str(i)+".png")
        while True:
            try:
                browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
                time.sleep(pause)
                newHeight = browser.execute_script("return document.documentElement.scrollHeight")
                if newHeight == lastHeight:
                    break
                lastHeight = newHeight
            except:
                break
            i += 1
            browser.get_screenshot_as_file("logs/image/test01_1_"+str(i)+".png")
    else:
        pause = 3
        lastHeight = browser.execute_script("return document.body.scrollHeight")
        i = 0
        browser.get_screenshot_as_file("logs/image/test01_1_"+str(i)+".png")
        while True:
            try:
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(pause)
                newHeight = browser.execute_script("return document.body.scrollHeight")
                if newHeight == lastHeight:
                    break
                lastHeight = newHeight
            except:
                break
            i += 1
            browser.get_screenshot_as_file("logs/image/test01_1_"+str(i)+".png")
    return scroll

# HÀM LẤY DỮ LIỆU TỪ LOOP
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

# ham load data custom 0
def Load_data_0(start,number,browser,data,data_save):
    if number==0:
        num=0
        while True:
            num+=1
            print(num)
            try:
                cache_dict={}
                for i in range(len(data['LOOP'])):
                    variable=data['LOOP'][i]
                    for value in variable.values():
                        value = value
                    for key in variable.keys():    
                        track_xpath_value = track_xpath(key)
                        kind_of_find,action,type_xpath=track_inf_xpath(track_xpath_value)
                        if action == 'click':
                            results=Find_xpath(browser,value,False)
                            Click_button(browser,results)
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
            except:
                print("website not found ...")
                break
        
    else:
        for i in range(start,number):
            print(i)
            try:
                cache_dict={}
                for i in range(len(data['LOOP'])):
                    variable=data['LOOP'][i]
                    for value in variable.values():
                        value = value
                    for key in variable.keys():    
                        track_xpath_value = track_xpath(key)
                        kind_of_find,action,type_xpath=track_inf_xpath(track_xpath_value)
                        if action == 'click':
                            results=Find_xpath(browser,value,False)
                            Click_button(browser,results)
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
            except:
                print("website not loading....")
                continue
            
    return data_save
# ham load data ytb
def Load_data_1(start,number,browser,data,data_save,columns):
    variable=data['LOOP'][0]
    for value in variable.values():
        value = value
    results=Find_xpath(browser,value,True)
    number=len(results)
    cache_list=[]
    for i in range(len(data['LOOP'])):
        try:
            variable=data['LOOP'][i]
            for value in variable.values():
                value = value
            for key in variable.keys():    
                track_xpath_value = track_xpath(key)
                kind_of_find,action,type_xpath=track_inf_xpath(track_xpath_value)
                if kind_of_find=='xpaths':
                    results=Find_xpath(browser,value,True)
                    var=get_data(results,True,type=type_xpath)
                    cache_list.append(var)
        except:
            print(data['LOOP'][i],"not found")
            continue
    for i in range(start,number):
        cache_dict={}
        for j in range(len(columns)):
            action=columns[j]
            cache_dict[action]=cache_list[j][i]
        data_save.append(cache_dict)
    return data_save

def load_data_2(start,number,browser,data,data_save,columns):
    cache_list=[]
    variable=data['LOOP'][0]
    for value in variable.values():
        value = value
    for key in variable.keys():    
        track_xpath_value = track_xpath(key)
        kind_of_find,action,type_xpath=track_inf_xpath(track_xpath_value)
    
    
    for i in range(start,number):
        cache_dict={}
        variable=data['LOOP'][i]
        try:
            for value in variable.values():
                value = value
            for key in variable.keys():    
                track_xpath_value = track_xpath(key)
                kind_of_find,action,type_xpath=track_inf_xpath(track_xpath_value)
                if action == 'click':
                    results=Find_xpath(browser,value,False)
                    Click_button(browser,results)
                else:
                    if kind_of_find=='xpaths':
                        results=Find_xpath(browser,value,True)
                        var=get_data(results,True,type=type_xpath)
                        cache_dict[action]=var
                    else:
                        results=Find_xpath(browser,value,False)
                        var=get_data(results,type=type_xpath)
                        cache_dict[action]=var
        except:
            continue
    data_save.append(cache_dict)
    return data_save

# HÀM LOAD FOR SAVE

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