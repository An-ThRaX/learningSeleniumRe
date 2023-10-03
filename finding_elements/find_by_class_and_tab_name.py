import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from basicWeb import url_letskodeit
class findByIdName():
    def test(self):
        driver = webdriver.Chrome()
        driver.get(url_letskodeit)
        driver.implicitly_wait(10)

        elementByClassName = driver.find_element(By.CLASS_NAME, "inputs")
        if elementByClassName is not None:
            print("element found -> by class")
            elementByClassName.send_keys("Testing")

        element_by_tab_name = driver.find_element(By.TAG_NAME, "a")
        # when selecting an element by CSS, different symbols represent different values
        # the pound symbol "#" == id
        if element_by_tab_name is not None:
            print("element found -> by tag" + element_by_tab_name.text)
        time.sleep(5)


run_tests = findByIdName()
run_tests.test()
