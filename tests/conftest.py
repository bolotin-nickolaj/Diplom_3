import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


@pytest.fixture(params=["chrome"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        service = Service(executable_path="/snap/bin/geckodriver")
        driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()
