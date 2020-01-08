import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b

class Collector:
	def __init__(self, driver):
		self.driver = driver
		#self.driver.get('https://www.instagram.com/unitytechnologies/')
	def get_followers(self):
		partisan = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')))
		partisan.click()

		popup = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]')))
		self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)

	def get_num_of_followers(self):
		
		partisan = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main')))
		s_partisan = b(partisan.get_attribute('innerHTML'), 'html.parser')
		#print(s_partisan) 
		followers = s_partisan.findAll('span', {'class': 'g47SY'})
		f = followers[1].getText().replace(',', '')
		if 'k' in f:
			f = float(f[:-1]) * 1000 # or multiplied by 10 ** 3
			return f
		elif  'm' in f:
			f = float(f[:-1]) * 1000000 # or multiplied by 10 ** 6
			return f
		else:
			return float(f)
	
	def get_num_of_post(self):
		
		post = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main')))
		s_post = b(post.get_attribute('innerHTML'), 'html.parser')
		#print(s_partisan) 
		post = s_post.findAll('span', {'class': 'g47SY'})
		p = post[0].getText().replace(',', '')
		if 'k' in p:
			p = float(p[:-1]) * 1000 # or multiplied by 10 ** 3
			return p
		elif  'm' in p:
			p = float(p[:-1]) * 1000000 # or multiplied by 10 ** 6
			return p
		else:
			return float(p)

	def get_num_of_following(self):
		
		following = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main')))
		s_following = b(following.get_attribute('innerHTML'), 'html.parser')
		#print(s_partisan) 
		following = s_following.findAll('span', {'class': 'g47SY'})
		fng = following[2].getText().replace(',', '')
		if 'k' in fng:
			fng = float(fng[:-1]) * 1000 # or multiplied by 10 ** 3
			return fng
		elif  'm' in fng:
			fng = float(fng[:-1]) * 1000000 # or multiplied by 10 ** 6
			return fng
		else:
			return float(fng)

		

