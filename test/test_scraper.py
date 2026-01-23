import unittest
from selenium import webdriver
from src import scraper
from src.job import JobType

class TestScraper(unittest.TestCase):

    def test_parse_site(self):
        pass

    def test_format_site_url(self):

        test_input = {
            'Abidjan': scraper.QueryParams (
                "Abidjan",
                "cleaner",
                1.0,
                1 ,
                10 ,
                JobType.FULL_TIME,
                "fr"
            ),
            'Ecatepec': scraper.QueryParams (
                "Ecatepec",
                "job_title",
                1.0,
                1 ,
                10 ,
                JobType.FULL_TIME,
                "mx"
            ),
            'Ibadan': scraper.QueryParams (
                "Ibadan",
                "job_title",
                1.0,
                1 ,
                10 ,
                JobType.FULL_TIME,
                "ng"
            ), 
            'MADRID': scraper.QueryParams (
                "MADRID",
                "job_title",
                1.0,
                1 ,
                10 ,
                JobType.FULL_TIME,
                "es"
            ),
            'Qingdao': scraper.QueryParams (
                "Qingdao",
                "job_title",
                1.0,
                1 ,
                10 ,
                JobType.FULL_TIME,
                "cn"

            ),
            'Ufa': scraper.QueryParams (
                "Ufa",
                "job_title",
                1.0,
                1 ,
                10 ,
                JobType.FULL_TIME,
                "ru"
            ),
            'Yangon': scraper.QueryParams (
                "Yangon",
                "job_title",
                1.0,
                1 ,
                10 ,
                JobType.FULL_TIME,
                "mm"
            )

        }
        test_expected = {
            'Abidjan': "",
            'Ecatepec':  "",
            'Ibadan': "",
            'MADRID':  "",
            'Qingdao': "",
            'Ufa':  "",
            'Yangon':  "",

        }

        for key in test_input.keys():
            self.assertEqual(
                test_expected[key],
                scraper.Scraper.format_site_url(test_input[key])
            )


        assert False

if __name__ == "__main__":
    unittest.main()