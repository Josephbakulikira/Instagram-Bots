import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b


#/html/body/div[4]/div/div[2]/ul/div/li[ 'x number ita ingiya apa' ]/div/div[2]/button xpath to follow button

class Interaction:
	def __init__(self, driver):
		self.driver = driver
	
	def follow(self):
		for x in range(1,21):
			time.sleep(2)
			try:
				follow = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/ul/div/li[%s]/div/div[2]/button'%(x))))
			except FileNotFoundError as fnferror:
				print(fnferror)
			except AssertionError as error:
				print(error)
			except:
				print("'you're probably blocked")
			
			follow.click()
			time.sleep(3600)
