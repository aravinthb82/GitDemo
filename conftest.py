import inspect, logging, pytest
from selenium import webdriver
from Data_Repository.HomePageData import HomePageDataContent

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browsername", action="store", default="chrome", help="which browser you want"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
#    capturebrowser = request.config.getoption("browsername")
#    if capturebrowser == "chrome":
    driver = webdriver.Chrome(executable_path="C:\\Users\\arvin\\Downloads\\BrowserDrivers\\chrome\\chromedriver_win32\\chromedriver.exe")
    #driver.get("https://www.rahulshettyacademy.com/#/index")
#       driver.maximize_window()
#    elif capturebrowser =="ff":
#        driver = webdriver.Firefox(executable_path="C:\\Users\\arvin\\Downloads\\BrowserDrivers\\geckodriver-v0.26.0-win64\\geckodriver.exe")
#        driver.get("https://www.rahulshettyacademy.com/angularpractice/")
#        driver.maximize_window()

    request.cls.driver = driver

