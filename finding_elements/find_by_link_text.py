from selenium import webdriver
from selenium.webdriver.common.by import By
from basicWeb import url_letskodeit
class findByIdName():
    def test(self):
        driver = webdriver.Chrome()
        driver.get(url_letskodeit)
        driver.implicitly_wait(10)

        elementByXpath = driver.find_element(By.LINK_TEXT, "HOME")
        # should always start with "a" tag == it's a link
        if elementByXpath is not None:
            print("element found -> by link text")

        elementByCss = driver.find_element(By.PARTIAL_LINK_TEXT, " COURSES")
        # when selecting an element by CSS, different symbols represent different values
        # the pound symbol "#" == id
        if elementByCss is not None:
            print("element found -> by partial link text")

run_tests = findByIdName()
run_tests.test()
