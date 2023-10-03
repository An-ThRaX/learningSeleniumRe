from selenium import webdriver
from selenium.webdriver.common.by import By
from basicWeb import url_letskodeit
class findByIdName():
    def test(self):
        driver = webdriver.Chrome()
        driver.get(url_letskodeit)
        driver.implicitly_wait(10)

        elementByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        if elementByXpath is not None:
            print("element found -> by xpath")

        elementByCss = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
        # when selecting an element by CSS, different symbols represent different values
        # the pound symbol "#" == id
        if elementByCss is not None:
            print("element found -> by css")

run_tests = findByIdName()
run_tests.test()
