from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, base_url="http://rozetka.com.ua/ua"):
        self.base_url = base_url
        self.driver = driver
    
    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)
    
    def get_title(self):
        return self.driver.title
    
    def get_url(self):
        self.driver.current_url
    
    def wait_element_to_click(self, locator):
        try:
            return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        except:
            self.driver.quit()
