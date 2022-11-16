import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://rozetka.com.ua/ua/")

time.sleep(10)
driver.quit()
