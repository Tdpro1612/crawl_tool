from source.body_crawler import *
from source.save_data import *
from source.custom_data import *
from source.extract_inf import *

# xử lý dữ liệu trong HARD

# path config
path = "config/config.yaml"
# load config và read config
data=load_configure(path)
# tạo file lưu
data_save=[]
# lấy column để lưu
columns=create_columns(data['LOOP'])
# lấy display cho extension
display=extract_extension(data)
extension=Extensions(display)
# tạo biến browser
browser=create_browser("chromdrive/chromedriver",chrome_options=extension)
# lấy url
url = track_url(data)
# mở website
open_website=Open_web(browser,url)
# cuộn trang
scroll=track_scroll(data)
if scroll != None:
    scroll=scroll_page(browser,scroll)
else:
    None
# kiểm tra có click mở rộng trang hay không   
for i in range(len(data['HARD'])):
        variable=data['HARD'][i]
        for value in variable.values():
            value = value
        for key in variable.keys():
            if 'xpath' in key:    
                track_xpath_value = track_xpath(key)
                kind_of_find,action,type_xpath=track_inf_xpath(track_xpath_value)
                if action == 'click':
                    results=Find_xpath(browser,value)
                    Click_button(browser,results)
# lấy số lượng row dữ liệu : number nếu có khai báo                
start,number=track_start(data),track_number(data)
# lấy số hiệu custom
custom=data.get('custom',None)

# xử lý dữ liệu trong LOOP
if custom == 0:
    Load_data_0(start,number,browser,data,data_save)
elif custom == 1:
    Load_data_1(start,number,browser,data,data_save,columns)
else:
    print("waiting i update ver 2 ....")

        
close_website=Close_web(browser)
# xử lý dữ liệu trong SAVE
type_save,path_save=track_save(data)
if type_save == 'xlsx':
    write_excel(path_save,data_save,columns=columns)
elif    type_save == 'json':
    write_json_beautifier(path_save,data_save)
else:
    write_csv(path_save,data_save,columns=columns)