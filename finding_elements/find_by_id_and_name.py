from selenium import webdriver
from selenium.webdriver.common.by import By
from basicWeb import url_letskodeit
class findByIdName():
    def test(self):
        driver = webdriver.Chrome()
        driver.get(url_letskodeit)
        driver.implicitly_wait(10)

        elementById = driver.find_element(By.ID, "displayed-text")
        if elementById is not None:
            print("element found -> by id")

        elementByName = driver.find_element(By.NAME, "show-hide")
        if elementByName is not None:
            print("element found -> by name")

run_tests = findByIdName()
run_tests.test()
