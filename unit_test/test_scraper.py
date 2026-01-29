import unittest
import backend.scraper as scraper
import backend.url_formatter as url_formatter
import backend.job as job
import os
import types

class Test_URL_Formatter(unittest.TestCase):

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
                "headless"          : None,
                "browser_version"   : "stable",
                "platform_name"     : "any",
                "timeout_timer"     : 1000
            },
            "driver_config2.json": {
                "driver"            : None,
                "headless"          : None,
                "browser_version"   : None,
                "platform_name"     : None,
                "timeout_timer"     : None
            },
            "driver_config3.json"   : None,
            "driver_config4.json"   : None,
            "driver_config5.json"   : None,
            "driver_config6.json"   : None,
            "driver_config7.json"   : None,
            "my_config.f"           : None,
            "nothing.c"             : None,
            "rewritein.rs"          : None,
            "shady.sh"              : None,
        }

        for  file in FILES:
            
            TEST_OBJ.config = None # clear object config
            TEST_OBJ.load_config(file)
            key = file.split("/")[-1]
            
            print(f"Testing {key}")

            self.assertEqual(
                TEST_OBJ.config,
                test_expected[key]
            )


