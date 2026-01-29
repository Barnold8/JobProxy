import unittest
import backend.scraper as scraper
import backend.url_formatter as url_formatter
import backend.job as job
import os

class Test_URL_Formatter(unittest.TestCase):

    def test_load_config(self):
        
        BASE_DIR = 'assets/tests/test_configs'
        ABS_PATH = os.path.join(os.getcwd(),BASE_DIR)
        FILES    = [f for f in os.listdir(ABS_PATH) if os.path.isfile(os.path.join(ABS_PATH, f))] # This is also our test_input
        TEST_OBJ = scraper.Scraper(scraper.Driver.CHROME)

        
        test_expected = [
            {
                "driver"            : "chrome",
                "headless"          : True,
                "browser_version"   : "stable",
                "platform_name"     : "any"
            }
        ]

        for index in (FILES):
            self.assertEqual(
                TEST_OBJ.load_config(FILES[index]),
                test_expected[index]
            )


