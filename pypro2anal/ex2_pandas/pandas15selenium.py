# Selenium 툴을 이용해 브라우저를 통제, 웹 크롤링 가능하다.
import time

from selenium import webdriver
'''
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get('https://daum.net')
browser.quit()
'''

'''
browser = webdriver.Chrome()
browser.get('http://www.google.com/xhtml');
search_box = browser.find_element("name", "q")
search_box.send_keys('파이썬')
search_box.submit()
time.sleep(5)
browser.quit()
'''

try:
    url = "https://www.daum.net"
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.get(url);
    browser.save_screenshot("daum_img.png")
    browser.quit()
    print('성공')
except Exception as e:
    print('에러', e)
