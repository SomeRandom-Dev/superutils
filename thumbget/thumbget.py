# thumbget.py from somerandompiggo's superutils under the MIT License

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

wholepage = False # this bool when switched to true will constantly scroll down until the end of the page has been reached. if the site has infinite scroll, this seems to crash. it is disabled by default

def getpage():
	driver.get("https://en.wikipedia.org/wiki/Main_Page")
	driver.refresh()
	if (wholepage == False):
		height = 720
	elif (wholepage == True):
		height = driver.execute_script("return document.body.parentNode.scrollHeight")
	driver.set_window_size(original_size['width'], height)
	driver.save_screenshot("page.png") # end filename
	driver.close()

options = Options()
options.add_argument("--headless") # this makes geckodriver headless meaning that no window pops up to screenshot. comment out this line to remove
driver = webdriver.Firefox(options=options,executable_path="/usr/bin/geckodriver")
driver.set_window_size(1280, 720)
original_size = driver.get_window_size()
getpage()

