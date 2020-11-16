from selenium import webdriver 
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options  
  
usr=input('Enter Email Address :')  
pwd=input('Enter Password:')  
  
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://zoom.us/signin') 
print ("Opened Zoom") 
sleep(1) 
  
username_box = driver.find_element_by_css_selector("#email")
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1) 


password_box = driver.find_element_by_css_selector('#password')
password_box.send_keys(pwd) 
print ("Password entered") 
sleep(1) 

login_box = driver.find_element_by_css_selector("#login-form > div:nth-child(4) > div > div.signin > button") 
login_box.click() 
  
print ("Done") 
input('Press anything to quit') 
driver.quit() 
print("Finished") 