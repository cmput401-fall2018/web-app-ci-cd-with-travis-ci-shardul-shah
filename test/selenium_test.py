from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import os 

# function that finds elements by ID 
def find_elem(elem_name, driver):
	driver.find_element_by_id(elem_name)

# the function that tests for each required element
def test_home():
	#driver = webdriver.Chrome() #for Mac OS

	option = Options()
	option.add_argument("headless")
	driverPath = os.getcwd() + '/chromedriver'
	driver = webdriver.Chrome(driverPath, options=option)

	driver.get("http://162.246.157.117:8000/")
	main_elems = [] 
	elem_names = ["name", "about", "skills", "milk", "education", "butter", "work", "contact"] # testing list
	#elem_names = ["name", "about", "skills", "education", "work", "contact"] # actual list

	for name in elem_names:
		try:
			find_elem(name, driver)
			main_elems.append((True, name,))
		except NoSuchElementException:
			main_elems.append((False, name,))

	for each in main_elems:
		try:
			assert each[0] != False
		except AssertionError:
			print("Missing " + each[1] + "; " + each[1] + " must exist.")
		
		
# run test function
test_home()
