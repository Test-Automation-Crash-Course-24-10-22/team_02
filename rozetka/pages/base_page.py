

class BasePage:

    def __init__(self, driver, base_url="https://rozetka.com.ua/ua/"):
        self.base_url = base_url
        self.driver = driver
    
    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)
    
    def get_title(self):
        return self.driver.title
    
    def get_url(self):
        self.driver.current_url
