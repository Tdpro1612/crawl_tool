from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from typing import *

def Extensions(display=False):
    chrome_options = Options()
    if display is True:   
        chrome_options.add_argument("--headless") #hide or not hide the website
        chrome_options.add_argument('disable_infobars') #hide the line Chrome is being controlled by automated software
    return chrome_options

def create_browser(executable_path: Text,chrome_options):
    executable_path="chromdrive\chromedriver.exe"
    """
    create the variable browser to do,
    executable_path nơi chứa file chrome drive đúng với version của chrome tải về tại đây https://sites.google.com/a/chromium.org/chromedriver/downloads
    """

    browser = webdriver.Chrome(executable_path,chrome_options=chrome_options)  

    return browser

def Open_web(browser,url):
    browser.get(url)   #open website
    pause = 3
    # time.sleep(20)      #stop time website to website load all ,you can fix number of second

# def Find_id(browser,id,many=False):
#     """
#     browser : variable to do
#     xpath : xpath to find the element in website
#     many : quantity the element to craw
#     """
#     if many is True:
#         variable=browser.find_elements_by_id(id)
#     else:
#         variable=browser.find_element_by_idh(id)
#     return variable

def Find_xpath(browser,xpath,many=False,*arg):
    """
    browser : variable to do
    xpath : xpath to find the element in website
    many : quantity the element to craw
    """
    if many is True:
        variable=browser.find_elements_by_xpath(xpath)
    else:
        variable=browser.find_element_by_xpath(xpath)
    return variable

# def Find_class(browser,classname,many=False):
#     """
#     browser : variable to do
#     classname : name to find the element in website
#     many : quantity the element to craw
#     """
#     if many is True:
#         variable=browser.find_elements_by_class_name(classname)
#     else:
#         variable=browser.find_element_by_class_name(classname)
#     return variable

def Click_button(variable):
    """
    variable : where to click
    """
    variable.click()

def Fill_blank(variable,value: Text):
    """
    variable : where to fill value 
    example :
    value : current_day = datetime(2021,8,14)
    variable.send_key("{}-{}-{}".format(current_day.day,current_day.month,current_day.year))
    """
    variable.clear()
    variable.send_keys(value)

def login(variable_user,user: Text,variable_password,password: Text):
    """
    you should create an account fake to craw if the web detect and block this account ,it no problem with you
    """
    variable_user.send_keys(user) # user name to fill
    variable_password.send_keys(password)    # password to fill

def Close_web(browser):
    browser.close()
    pass


# if __name__=="__main__":
#     a=Extensions()
#     b=create_browser('chromdrive/chromedriver',a)
#     c=Open_web(b,"https://www.vncreatures.net/kqtracuu.php?page=25&type=nhom&loai=1&")
#     e=Find_class(b,"aLink02",True)
#     for i in e:
#         print(i.text)
#     d=Close_web(b)