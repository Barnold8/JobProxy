from typing import List
from enum import Enum
from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from job import JobSite, QueryParams
import url_formatter

class Driver(Enum):
    FIREFOX = 1
    CHROME = 2

class Scraper:

    def __init__(self,driver_type:Driver):
        self.driver = None
        self.init_driver(driver_type)

    def init_driver(self,driver_type:Driver) -> None:
        # Function not tested since its just variable assingment which is handled by external code (selenium)
        match driver_type:
            case Driver.FIREFOX:
                self.driver = webdriver.Firefox()
            case Driver.CHROME:
                self.driver = webdriver.Chrome()

    def parse_site(self,url:str,params:List[str])-> None: # todo: add Job type
        pass

    def format_site_url(job_site:JobSite,params:QueryParams)-> str:
        return url_formatter.URL_Formatter.format_url(job_site,params)

# def foo():
#     s = Scraper(Driver.FIREFOX)
#     s.format_site_url("reed","")
