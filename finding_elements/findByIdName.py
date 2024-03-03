from selenium import webdriver
from selenium.webdriver.common.by import By


class FindByIdName:
    def test(self):
        baseUrl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.get(baseUrl)

        driver.implicitly_wait(10)

        elementById = driver.find_element(By.ID, 'displayed-text')
        if elementById is not None:
            print('Element found -> By Id')

        elementByName = driver.find_element(By.NAME, 'show-hide')
        if elementByName is not None:
            print('Element found -> By Name')



test_run = FindByIdName()
test_run.test()
