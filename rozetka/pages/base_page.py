class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        self.driver.get(url)
