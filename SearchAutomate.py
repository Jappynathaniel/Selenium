from selenium import  webdriver 
import time 
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By 
driver = webdriver.Chrome(r"C:\Users\Jasper Nathaniel J\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\selenium\webdriver\chrome\chromedriver_win32\chromedriver.exe")
driver.maximize_window() 
driver.get("https://www.google.com/")
driver.find_element(By.NAME,"q").send_keys("Jasper Nathaniel")
driver.find_element(By.NAME,"btnK").send_keys(Keys.ENTER)
driver.close()
time.sleep(10)
print("Automation is complete...")
