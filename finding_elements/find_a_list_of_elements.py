import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from basicWeb import url_letskodeit
class findByIdName():
    def test(self):
        driver = webdriver.Chrome()
        driver.get(url_letskodeit)
        driver.implicitly_wait(10)

        element_list_by_class_name = driver.find_elements(By.CLASS_NAME, "inputs")
        length1 = len(element_list_by_class_name)

        if element_list_by_class_name is not None:
            print(f"element found -> by class name: {str(length1)} elements")

        element_list_by_tab_name = driver.find_elements(By.TAG_NAME, "td")
        length2 = len(element_list_by_tab_name)
        if element_list_by_tab_name is not None:
            print(f"element found -> by tag name: {str(length2)} elements")


run_tests = findByIdName()
run_tests.test()
