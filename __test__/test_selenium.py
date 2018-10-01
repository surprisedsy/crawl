import time

from selenium import webdriver

wd = webdriver.Chrome("D:/Programming/04 IoT2018/chromedriver_win32/chromedriver.exe")
wd.get("http://www.google.com")
time.sleep(5)

html = wd.page_source
print(html)

wd.quit()