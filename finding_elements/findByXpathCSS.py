from selenium import webdriver
from selenium.webdriver.common.by import By


class FindXpathCSS:
    def test(self):
        baseUrl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.get(baseUrl)


        elementByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        if elementByXpath is not None:
            print('Element found -> By Xpath')

        elementByCss = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
        if elementByCss is not None:
            print('Element found -> By CSS')




test_run = FindXpathCSS()
test_run.test()
