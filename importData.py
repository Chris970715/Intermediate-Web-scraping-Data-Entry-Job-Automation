import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



class ImportData:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        chrome_driver_path = "C:\python_bot\chromedriver.exe"
        service = Service(executable_path=chrome_driver_path)

        self.driver = webdriver.Chrome(service=service, options=options)


    def send_data(self,par):

        for index in range(len(par["prices"])):
            self.driver.get(par["url"])

            time.sleep(1)
            inputs = self.driver.find_elements(By.CSS_SELECTOR, ".Xb9hP input")
            button = self.driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span")
            time.sleep(1)

            inputs[0].click()
            inputs[0].send_keys(par["prices"][index])
            inputs[1].click()
            inputs[1].send_keys(par["links"][index])
            inputs[2].click()
            inputs[2].send_keys(par["addresses"][index])

            button.click()


    def closeWeb(self):
        self.driver.quit()