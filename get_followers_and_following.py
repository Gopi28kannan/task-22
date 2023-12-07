from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Text:
     def __init__(self,url):
          self.url=url
          self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

     def getting_follow(self):
          try:
               self.driver.get(self.url)
               time.sleep(2)
               self.driver.maximize_window()
               time.sleep(1)
               # I have use only xpath  and contains method, but this mehod all times not perfectly worked.
               followers=self.driver.find_element (By.XPATH,'//*[contains(text(), "followers")]').text
               following=self.driver.find_element (By.XPATH,'//*[contains(text(), "following")]').text
               print(followers ,' and ',following)
          except:
               print("error")
          finally:
               print("Run successfully")
               
     def shutdown(self):
          time.sleep(2)
          #after 2 seconds sleep next close window
          self.driver.quit()
url='https://www.instagram.com/guviofficial/'
follow=Text(url)
follow.getting_follow()
follow.shutdown()
