from source.body_crawler import *
from source.save_data import *
from source.custom_data import *
from source.extract_inf import *
import yaml
path = "config/config.yaml"
data=load_configure(path)
data_save=[]
columns=create_columns(data['LOOP'])
display=extract_extension(data)
extension=Extensions(display)

browser=create_browser("chromdrive\chromedriver.exe",chrome_options=extension)
url = track_url(data)
open_website=Open_web(browser,url)
scroll=track_scroll(data)
if scroll != None:
    scroll=scroll_page(browser,scroll)
else:
    None
start,number=track_start(data),track_number(data)

if number==0:
    variable=data['LOOP'][0]
    for value in variable.values():
        value = value
    results=Find_xpath(browser,value,True)
    number=len(results)
    data_save=load_data_ytb(start,number,browser,data,data_save,columns)
    
        
else:
    data_save=Load_data(start,number,browser,data,data_save)

        
close_website=Close_web(browser)
type_save,path_save=track_save(data)
if type_save == 'xlsx':
    write_excel(path_save,data_save,columns=columns)
elif    type_save == 'json':
    write_json_beautifier(path_save,data_save)
else:
    write_csv(path_save,data_save,columns=columns)