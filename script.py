import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import login
import collector
import interaction

driver = 0

username = ''  #enter your userame here
password = '' # enter your password here

def main():
	global driver 

	print("processing!")
	driver = webdriver.Chrome("D:/chromedriver.exe")
	l = login.Login(driver, username, password)
	l.signin()
	driver.get('https://www.instagram.com/unitytechnologies/')
	
	col = collector.Collector(driver)
	col.get_followers()
	print("followers: ", col.get_num_of_followers())
	print("post: ", col.get_num_of_post())
	print("following: ", col.get_num_of_following())

	followButton = interaction.Interaction(driver)
	followButton.follow()


	time.sleep(60)

if __name__ == "__main__":
	main()

