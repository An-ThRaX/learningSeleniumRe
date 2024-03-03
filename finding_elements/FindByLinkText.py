from selenium import webdriver
from selenium.webdriver.common.by import By


class FindXpathCSS:
    def test(self):
        baseUrl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.get(baseUrl)


        elementByLinkText = driver.find_element(By.LINK_TEXT, "HOME")
        if elementByLinkText is not None:
            print('Element found -> By LINK_TEXT')

        elementByPartialLink = driver.find_element(By.PARTIAL_LINK_TEXT, "COURSES")
        if elementByPartialLink is not None:
            print('Element found -> By PARTIAL_LINK_TEXT')




test_run = FindXpathCSS()
test_run.test()
