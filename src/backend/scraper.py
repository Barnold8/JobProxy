from typing import List, Any
from enum import Enum
# from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from backend.job import JobSite, QueryParams
from backend import url_formatter
from typing import Optional

class Driver(Enum):
    FIREFOX = 1
    CHROME = 2

class Scraper:

    def __init__(self,driver_type:Driver):
        self.driver: Optional[WebDriver] = None
        self.init_driver(driver_type)

    def init_driver(self,driver_type:Driver):
        # Function not tested since its just variable assingment which is handled by external code (selenium)
        match driver_type:
            case Driver.FIREFOX:
                self.driver = webdriver.Firefox()
            case Driver.CHROME:
                self.driver = webdriver.Chrome()

    def parse_site(self,url:str,params:List[str])-> None:
        pass

    def load_config(self, path:str) -> None:
        pass

    @staticmethod
    def format_site_url(job_site:JobSite,params:QueryParams)-> str:
        return url_formatter.URL_Formatter.format_url(job_site,params)
