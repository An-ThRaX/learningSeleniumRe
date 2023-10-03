from selenium import webdriver
from selenium.webdriver.common.by import By
from basicWeb import url_letskodeit


class FindPrices:
    # find  the price of a specific course
    def test(self):
        driver = webdriver.Chrome()
        driver.get(url_letskodeit)
        driver.implicitly_wait(10)
        driver.maximize_window()

        find_the_required_price = driver.find_element(By.XPATH,
          "//table[@id='product']//td[text()='Python Programming Language']//following-sibling::td")

        if find_the_required_price.text == '30':
            print("all clear")


run_tests = FindPrices()
run_tests.test()

class FindAuthor:
    # find the author of the book "The Green Mile"
    def test(self):
        driver = webdriver.Chrome()
        driver.get("https://dhtmlx.com/docs/products/dhtmlxGrid/")
        driver.implicitly_wait(10)
        driver.maximize_window()

        find_author = driver.find_element(By.XPATH,
            "//div[@id='layout']//div[contains(text(), 'The Green Mile')]//following-sibling::div[1]")



