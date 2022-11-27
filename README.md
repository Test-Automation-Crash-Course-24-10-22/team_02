# team_02
- - -
### Selenium set up :
1. Clone the repository to your local machine.
2. Create venv with the command : `python -m venv venv` and activate it (venv\Scripts\activate.bat)
3. Install all necessary packages with the command : `pip install -r requirements.txt`
4. Run website in folder /selenium_setup : `python setup.py`
- - -
### Informations :
1. https://selenium-python.readthedocs.io/index.html
2. https://www.selenium.dev/documentation/
- - - 
### Run tests :
For unittest : run all tests - `python -m unittest` | run certain test - `python -m unittest tests.test_logout`
For pytest   : run all tests - `pytest tests`       | run certain test - `pytest tests/test_logout.py`
- - -
### Generate report :
Use the command : `pytest tests --html=report.html --self-contained-html`
- - -