from selenium import webdriver
from userInfo import email, password
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import *
import time

class Browser:
  
  def __init__(self, email, password):
    self.browser = webdriver.Chrome()
    self.email = email
    self.password = password

  def goHepsiburada(self):
    self.browser.get("https://www.hepsiburada.com/")
    time.sleep(10)
    
    signinFlow = self.browser.find_element_by_xpath("//*[@id='myAccount']")
    ActionChains(self.browser).click(signinFlow).perform()

    signinBtn = self.browser.find_element_by_xpath("//*[@id='login']")
    ActionChains(self.browser).click(signinBtn).perform()
    
  def signinBox(self):
    self.browser.get(self.browser.current_url)
    time.sleep(3)
    self.browser.find_element_by_xpath("//*[@id='email']").send_keys(self.email)
    self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)
    self.browser.find_element_by_css_selector("#form-login > div.form-actions > button").click()

userDeniz = Browser(email,password)
userDeniz.goHepsiburada()
userDeniz.signinBox()