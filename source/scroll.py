import selenium
import time
from selenium import webdriver

browser = webdriver.Chrome("chromedrive/chromedriver")
browser.get("https://www.youtube.com/watch?v=PvTHRMLE3W4")
print(browser.title)

pause = 3
jav_scrip_ytb = "document.documentElement.scrollHeight"
jav_scrip_tw_fb = "document.body.scrollHeight"
lastHeight = browser.execute_script("return document.documentElement.scrollHeight")
print(lastHeight)
i = 0
browser.get_screenshot_as_file("logs/image/test01_1_"+str(i)+".png")
while True:
	try:
		browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
		time.sleep(pause)
		newHeight = browser.execute_script("return document.documentElement.scrollHeight")
		print(newHeight)
		if newHeight == lastHeight:
			break
		lastHeight = newHeight
	except:
		break
	i += 1
	browser.get_screenshot_as_file("logs/image/test01_1_"+str(i)+".png")

browser.quit()