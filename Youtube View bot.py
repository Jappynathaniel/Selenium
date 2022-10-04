from selenium import webdriver 
import time 
count = int(input("Enter the number :"))
ref = int(input("refresh time (in secs):"))
url=input("Type or Paste the link : ")
drive = []
for i in range (count):  
        drive.append(webdriver.Chrome(r"C:\Users\Jasper Nathaniel J\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\selenium\webdriver\chrome\chromedriver_win32\chromedriver.exe")) #
        drive[i].get(url)
while True: 
     time.sleep(ref)
     drive[i].refresh() 
