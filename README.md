# team_02
- - -
### Description :
In this project **Rozetka Website** is automated testing.

This project provides an UI testing with Selenium WebDriver, using Page Object Model design pattern.
- - -
### Framework Overview :
The **Page Object Model** means that each individual webpage has its own class, each containing the methods specific to controls on the  page.
Thus, each page is independent and separate from the tests, meaning any changes to the page are isolated to only the corresponding page class.
This makes for code that is cleaner, easier to read and maintain, and contains less duplication.
- - -
### Technologies :
- Selenium
- Webdriver manager
- Unittest
- - -
### Execute Tests:
1. To run the project first make sure you have python installed in your system if not please install python
2. Clone the repository to your local machine
3. Create venv with the command `python -m venv venv` and activate it
4. Install all the necessary packages with the command `pip install -r requirements.txt`
5. Add file **credentials** into **config** dir with your **email** and **password** from rozetka-website (`EMAIL="example@gmail.com", PASSWORD="example"`)
6. Run tests :
    - using **unittest** : 
        - all : `python -m unittest`
        - certain : `python -m unittest tests.test_logout`
    - using **pytest** : 
        - all : `pytest tests`
        - certain : `pytest tests/test_logout.py`
- - -
### Allure reports :
1. Obtain the folder **allure_reports**
2. See reports with the command `allure serve allure_reports`
- - -
### Information links :
- [Selenium documentation 1](https://selenium-python.readthedocs.io/index.html)
- [Selenium documentation 2](https://www.selenium.dev/documentation/)
- [Allure documentation](https://docs.qameta.io/allure/)
- - -