import json
import os
from typing import List, Any
from enum import Enum
# from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options as default_chrome_options
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from backend.job import JobSite, QueryParams
from backend import url_formatter
from typing import Optional

class Driver(Enum):
    FIREFOX = 1
    CHROME = 2

class Scraper:

    def __init__(self,driver_type:Driver,config_path:str):
        
        self.driver: Optional[WebDriver] = None
        self.config: Optional[dict]      = None

        self.load_config(config_path)
        self.init_driver(driver_type)

    def init_driver(self,driver_type:Driver):
        # Function not tested since its selenium handling this, related code to influence it is tested
        match driver_type:
            case Driver.FIREFOX:
                self.driver = webdriver.Firefox()
                firefox_options = webdriver.FirefoxOptions()
                
            case Driver.CHROME:
                self.driver = webdriver.Chrome()
                chrome_options = default_chrome_options


    def parse_site(self,url:str,params:List[str])-> None:
        pass

    def load_config(self, path:str) -> None:

        REQUIRED_FIELD_COUNT = 5

        if os.path.getsize(path) <= 0:
            return
        try:
            with open(path,"r") as file:
                data = json.load(file)
                if len(data) < REQUIRED_FIELD_COUNT: # max required fields for a config file to be valid
                    return 
                self.config = data
        except FileNotFoundError as fnfe:
            print(f"Error while trying to open {path}\n\n\t{fnfe}")


    @staticmethod
    def format_site_url(job_site:JobSite,params:QueryParams)-> str:
        return url_formatter.URL_Formatter.format_url(job_site,params)
