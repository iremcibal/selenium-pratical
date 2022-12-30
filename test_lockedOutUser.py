# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from constants import *

## locked_out_user ile giriş yapıldığında verilen uyarı mesajının doğrulanması
class TestLockedOutUser():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_lockedOutUser(self):
    self.driver.get(BASE_URL)
    self.driver.maximize_window()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, LOCKED_OUT_USERNAME)))
    self.driver.find_element(By.CSS_SELECTOR, LOCKED_OUT_USERNAME).send_keys(LOCKED_OUT_USERNAME_KEYS)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, PASSWORD)))
    self.driver.find_element(By.CSS_SELECTOR, PASSWORD).send_keys(PASSWORD_KEYS)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, LOGIN_BUTTON)))
    self.driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON).click()
    assert self.driver.find_element(By.CSS_SELECTOR,ERROR_ALERT ).text == LOCKED_OUT_ERROR_TEXT;
  
