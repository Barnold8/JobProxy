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



def is_version_number(version_string:str)->bool:

    digits = version_string.split(".")

    for num in digits:
        if num.isnumeric() == False:
            return False
    else:
        return True

class Driver(Enum):
    FIREFOX = 1
    CHROME = 2

class Scraper:

    def __init__(self,config_path:str):
        
        self.driver: Optional[WebDriver] = None
        self.config: Optional[dict]      = None

        self.load_config(config_path)

        match self.config["driver"]:

            case "chrome":
                self.init_driver(Driver.CHROME)
            case "firefox":
                self.init_driver(Driver.FIREFOX)
            case _:
                self.init_driver(Driver.CHROME)

    def init_driver(self,driver_type:Driver):
        # Function not tested since its selenium handling this, related code to influence it is tested
        match driver_type:
            case Driver.FIREFOX:

                firefox_options = self.apply_options(webdriver.FirefoxOptions())
                self.driver = webdriver.Firefox(options=firefox_options)
                self.driver.set_page_load_timeout(self.config["timeout_timer"])

            case Driver.CHROME:
                
                chrome_options = self.apply_options(default_chrome_options())
                self.driver = webdriver.Chrome(options=chrome_options)
                self.driver.set_page_load_timeout(self.config["timeout_timer"])
                
    def apply_options(self,options): # not sure if i should test this since its just setting values in selenium codebase
        options_copy = options
        # options_copy.platform_name = self.config["platform_name"] # causes crash for firefox driver, might remove

        if self.config["headless"]:
            if self.config["driver"] == "firefox":
                options_copy.add_argument("--headless")
            elif self.config["driver"] == "chrome":
                options_copy.add_argument("--headless=new")
        options_copy.browser_version = self.config["browser_version"]

        return options_copy

    def parse_site(self,url:str,params:List[str])-> None:
        pass

    def verify_config(self,config: dict):
        if config is None:
            self.config = None

        config_copy = dict(config) 

        rules = {
            "driver": {
                "default": "chrome",
                "allowed": {"chrome", "firefox"},
                "coerce": lambda v: v.lower() if isinstance(v, str) else v,
            },
            "headless": {
                "default": True,
                "coerce": lambda v: (
                    v.lower() == "true" if isinstance(v, str) else v
                ),
                "validate": lambda v: isinstance(v, bool),
            },
            "browser_version": {
                "default": "stable",
                "validate": lambda v: (
                    isinstance(v, str)
                    and (v.lower() == "stable" or is_version_number(v))
                ),
            },
            "platform_name": {
                "default": "any",
                "allowed": {"any"},
                "coerce": lambda v: v.lower() if isinstance(v, str) else v,
            },
            "timeout_timer": {
                "default": 5000,
                "validate": lambda v: isinstance(v, int) and v >= 0,
            },
        }

        for key, rule in rules.items():
            value = config_copy.get(key)

            if value is None:
                config_copy[key] = rule["default"]
                continue

            if "coerce" in rule:
                value = rule["coerce"](value)

            if "allowed" in rule and value not in rule["allowed"]:
                config_copy[key] = rule["default"]
                continue

            if "validate" in rule and not rule["validate"](value):
                config_copy[key] = rule["default"]
                continue

            config_copy[key] = value

        self.config = config_copy  

    def load_config(self, path:str) -> None:

        REQUIRED_FIELD_COUNT = 5
        
        if os.path.getsize(path) <= 0 or path.split(".")[-1].lower() != "json":
            return
        try:
            with open(path,"r") as file:
                
                data = json.load(file)

                if len(data) < REQUIRED_FIELD_COUNT: # max required fields for a config file to be valid
                    return 

                self.verify_config(data)

        except FileNotFoundError as fnfe:
            print(f"Error while trying to open {path}\n\n\t{fnfe}")


    @staticmethod
    def format_site_url(job_site:JobSite,params:QueryParams)-> str:
        return url_formatter.URL_Formatter.format_url(job_site,params)
