# import time
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# main_path = os.path.abspath('')+'\\'
# print(main_path,'main_path')

# # Replace 'chromedriver-sel\\chromedriver' with the actual path to your chromedriver executable
# driver = webdriver.Chrome(service=Service('chromedriver-sel\\chromedriver.exe'))
# driver.get('http://www.google.com/')

# time.sleep(5) # Let the user actually see something!

# search_box = driver.find_element_by_name('q')


# search_box.send_keys('ChromeDriver')

# search_box.submit()

# time.sleep(5) # Let the user actually see something!

# driver.quit()
import datetime
print('red'+str(datetime.datetime.now()))