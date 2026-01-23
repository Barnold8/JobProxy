from enum import Enum
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Driver(Enum):
    FIREFOX = 1
    CHROME = 2

class Scraper:

    def __init__(self,driver_type:Driver):
        self.driver = self.init_driver(driver_type)

    def init_driver(self,driver_type:Driver)-> None:
        # Function not tested since its just variable assingment which is handled by external code (selenium)
        match driver_type:
            case Driver.FIREFOX:
                self.driver = webdriver.Firefox()
            case Driver.CHROME:
                self.driver = webdriver.Chrome()
        

