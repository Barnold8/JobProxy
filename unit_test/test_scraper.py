import unittest
import backend.scraper as scraper
import backend.url_formatter as url_formatter
import backend.job as job
import os
import types

class Test_Scraper(unittest.TestCase):

    def test_is_version_number(self):
        test_input = { # generated using assets/helper_scripts/generate_version_numbers.py
            "Test0": "__-__---__--.__-__---__--.invalid",
            "Test1": "2.3.6",
            "Test2": "4.6.7",
            "Test3": "6.8.9",
            "Test4": "6.2.2",
            "Test5": "-3.-8.asdmkasdmasd",
            "Test6": "2.9.2",
            "Test7": "4.2.6",
            "Test8": "2.9.7",
            "Test9": "9.4.5",
            "Test10": "asdmkasdmasd.-3.-2",
            "Test11": "3.1.5",
            "Test12": "9.4.8",
            "Test13": "4.2.4",
            "Test14": "1.1.2",
            "Test15": "\n\n\n.-3.",
            "Test16": "8.3.5",
            "Test17": "-7.asdmkasdmasd.asdmkasdmasd",
            "Test18": "-7.__-__---__--.__-__---__--",
            "Test19": "9.9.4",
        }

        test_expected = { 
            "Test0": False,
            "Test1": True,
            "Test2": True,
            "Test3": True,
            "Test4": True,
            "Test5": False,
            "Test6": True,
            "Test7": True,
            "Test8": True,
            "Test9": True,
            "Test10": False,
            "Test11": True,
            "Test12": True,
            "Test13": True,
            "Test14": True,
            "Test15": False,
            "Test16": True,
            "Test17": False,
            "Test18": False,
            "Test19": True,
        }

        for key in test_input.keys():

            self.assertEqual(
                scraper.is_version_number(test_input[key]),
                test_expected[key]
            )

    def test_verify_config(self):

        TEST_OBJ = object.__new__(scraper.Scraper)

        test_input = {
            "driver_config0.json" : {
                "driver"            : "chrome",
                "headless"          : True,
                "browser_version"   : "stable",
                "platform_name"     : "any",
                "timeout_timer"     : 5000
            },
            "driver_config1.json" : {
                "driver"            : "chrome",
                "headless"          : None,
                "browser_version"   : "stable",
                "platform_name"     : "any",
                "timeout_timer"     : 1000
            },
            "driver_config2.json" : {
                "driver"            : None,
                "headless"          : None,
                "browser_version"   : None,
                "platform_name"     : None,
                "timeout_timer"     : None
            },
            "driver_config3.json" : {
                "driver"            : "chrome"
            },
            "driver_config4.json" : {},
            "driver_config5.json" : {
                "driver"            : "chrome",
                "headless"          : True,
                "browser_version"   : "stable"
            },
            "driver_config6.json" : {
                "driver"            : "chrome",
                "headless"          : True,
                "browser_version"   : "stable",
                "platform_name"     : "any",
                "timeout_timer"     : -100
            },
            "driver_config7.json" : {
                "driver"            : "chrome",
                "headless"          : "True",
                "browser_version"   : "stable",
                "platform_name"     : "any",
                "timeout_timer"     : -100
            },
        }

        test_expected = {
            "driver_config0.json" : {
                "driver"            : "chrome",
                "headless"          : True,
                "browser_version"   : "stable",
                "platform_name"     : "any",
                "timeout_timer"     : 5000
            },
            "driver_config1.json" : {
                "driver"            : "chrome",
                "headless"          : True,
                "browser_version"   : "stable",
                "platform_name"     : "any",
                "timeout_timer"     : 1000
            },
            "driver_config2.json" : {
                "driver"            : "chrome",
                "headless"          : True,
                "browser_version"   : "stable",
                "platform_name"     : "any",
                "timeout_timer"     : 5000
            },
            "driver_config3.json" : {
                "driver"            : "chrome",
                "headless"          : True,
                "browser_version"   : "stable",
                "platform_name"     : "any",
                "timeout_timer"     : 5000
            },
            "driver_config4.json" : {  
                "driver"            : "chrome",
                "headless"          : True,
                "browser_version"   : "stable",
                "platform_name"     : "any",
                "timeout_timer"     : 5000
                },
            "driver_config5.json" :  {  
                "driver"            : "chrome",
                "headless"          : True,
                "browser_version"   : "stable",
                "platform_name"     : "any",
                "timeout_timer"     : 5000
                },
            "driver_config6.json" : {
                "driver"            : "chrome",
                "headless"          : True,
                "browser_version"   : "stable",
                "platform_name"     : "any",
                "timeout_timer"     : 5000
            },
            "driver_config7.json" : {
                "driver"            : "chrome",
                "headless"          : True,
                "browser_version"   : "stable",
                "platform_name"     : "any",
                "timeout_timer"     : 5000
            },
        }

        for key in test_input.keys():

            TEST_OBJ.config = None # clear previous config
            TEST_OBJ.verify_config(test_input[key])
            self.assertEqual(
                TEST_OBJ.config,
                test_expected[key]
            )

    def test_load_config(self):
        
        BASE_DIR = 'assets/tests/test_configs'
        ABS_PATH = os.path.join(os.getcwd(),BASE_DIR)
        FILES    = [os.path.join(os.getcwd(),f"{BASE_DIR}/{f}") for f in os.listdir(ABS_PATH) if os.path.isfile(os.path.join(ABS_PATH, f))] # This is also our test_input
        TEST_OBJ = object.__new__(scraper.Scraper)

        test_expected = {
            "driver_config.bat" : None,
            "conf.ini": None,
            "driver_config0.json": {
                "driver"            : "chrome",
                "headless"          : True,
                "browser_version"   : "stable",
                "platform_name"     : "any",
                "timeout_timer"     : 5000
            },
            "driver_config1.json": {
                "driver"            : "chrome",
                "headless"          : True,
                "browser_version"   : "stable",
                "platform_name"     : "any",
                "timeout_timer"     : 1000
            },
            "driver_config2.json": {
                "driver"            : "chrome",
                "headless"          : True,
                "browser_version"   : "stable",
                "platform_name"     : "any",
                "timeout_timer"     : 5000
            },
            "driver_config3.json"   : None,
            "driver_config4.json"   : None,
            "driver_config5.json"   : None,
            "driver_config6.json"   : {
                "driver"            : "chrome",
                "headless"          : True,
                "browser_version"   : "stable",
                "platform_name"     : "any",
                "timeout_timer"     : 5000
            },
            "driver_config7.json"   : {
                "driver"            : "chrome",
                "headless"          : True,
                "browser_version"   : "stable",
                "platform_name"     : "any",
                "timeout_timer"     : 5000
            },
            "my_config.f"           : None,
            "nothing.c"             : None,
            "rewritein.rs"          : None,
            "shady.sh"              : None,
        }

        for  file in FILES:
            
            TEST_OBJ.config = None # clear object config
            print(f"Loading {file}")
            TEST_OBJ.load_config(file)
            key = file.split("/")[-1]
            print(f"Testing {key}")
            
            self.assertEqual(
                TEST_OBJ.config,
                test_expected[key]
            )

    def test_parse_site(self):
        pass

    def test_grab_jobs(self):
        _scraper = scraper.Scraper("assets/configs/driver_config.json") # use default config file to intiialise scraper

        directories = [x[0] for x in os.walk("assets/tests/test_sites/")]
        directories = [f"{os.getcwd()}\\{x}\\page1.html" for x in directories if x[-1].isnumeric()] # gets all "root" website searches

        test_instances = {
            "test1": job.JobSiteDetails(
                job_card_id      = ".job-container",
                job_title_id     = "[id=\"job-title\"]",
                job_salary_id    = "[data-salary]",
                job_location_id  = ".JOB-LOCATION",
                job_poster_id    = ".job-poster",
                job_posted_on_id = ".job-since-posted",
                job_href_id      = ".job-application-link a",
                job_time_id      = ".job-Time-descriptor",
                job_next_page_id = ".Next a"
            ),
            "test2": job.JobSiteDetails(
                job_card_id      = ".job-container",
                job_title_id     = "[id=\"job-title\"]",
                job_salary_id    = "[data-salary]",
                job_location_id  = ".JOB-LOCATION",
                job_poster_id    = ".job-poster",
                job_posted_on_id = ".job-since-posted",
                job_href_id      = ".job-application-link a",
                job_time_id      = ".job-Time-descriptor",
                job_next_page_id = ".Next a"
            ),
        }

        test_expected = {
            "test1": [
                job.Job(
                    job_title="Unit test writer (god help them)",
                    job_salary="12-1000",
                    job_location="Morthal",
                    job_poster="Job Jobbington",
                    job_posted_on="4 days ago",
                    job_time="Part time",
                    job_href="www.google.com"
                ),
                job.Job(
                    job_title="Cleaner",
                    job_salary="1-2",
                    job_location="San Fransisco",
                    job_poster="Job",
                    job_posted_on="1 month ago",
                    job_time="Full time",
                    job_href="www.google.com"
                ),
                job.Job(
                    job_title="Some type of job",
                    job_salary="N/A",
                    job_location="...",
                    job_poster="Job Jobbington1",
                    job_posted_on="25 days ago",
                    job_time="Comes in once a week",
                    job_href="www.google.com"
                ),
                job.Job(
                    job_title="2fa enthusiast",
                    job_salary="2fa",
                    job_location="Whitechapel",
                    job_poster="Your local jobbery",
                    job_posted_on="32 seconds ago",
                    job_time="24/7",
                    job_href="www.google.com"
                ),
                job.Job(
                    job_title="Data Analyst",
                    job_salary="1-2",
                    job_location="RivErw0od",
                    job_poster="The job man",
                    job_posted_on="1 hour ago",
                    job_time="Training",
                    job_href="www.google.com"
                ),
                job.Job(
                    job_title="Some type of job",
                    job_salary="N/A",
                    job_location="...",
                    job_poster="Jobs r us",
                    job_posted_on="Just now",
                    job_time="Comes in once a week",
                    job_href="www.google.com"
                ),
                job.Job(
                    job_title="Unit test writer (god help them)",
                    job_salary="12-1000",
                    job_location="Morthal",
                    job_poster="Job Jobbington",
                    job_posted_on="3 month ago",
                    job_time="Part time",
                    job_href="www.google.com"
                ),
                job.Job(
                    job_title="Cleaner",
                    job_salary="1-2",
                    job_location="San Fransisco",
                    job_poster="The jobsmith",
                    job_posted_on="9 days ago",
                    job_time="Full time",
                    job_href="www.google.com"
                ),
                job.Job(
                    job_title="Some type of job",
                    job_salary="N/A",
                    job_location="...",
                    job_poster="Not provided",
                    job_posted_on="1 year ago",
                    job_time="Comes in once a week",
                    job_href="www.google.com"
                ),
            ],
            "test2": [

            ]
        }

        # TODO: write tests for site "test2"
        for directory in directories:
            _scraper.driver.get(directory)                      # synthesis making request to job site 
            test_site = directory.split("/")[-1].split("\\")[0] # get the test site key from the directory we are in
            test_instance = test_instances[test_site]           # the reference instance
            j = _scraper.grab_jobs(test_instance)               # list of jobs grabbed
            self.assertEqual(
                j,
                test_expected[test_site]
            )