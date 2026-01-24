import unittest
import src.scraper as scraper
import src.job as job



class TestScraper(unittest.TestCase):

    def test_parse_site(self):
        pass

    def test_format_site_url_INDEED(self):

        test_input = {
            'Abidjan': scraper.QueryParams (
                "Abidjan",
                "cleaner",
                -10,
                1 ,
                10 ,
                job.JobType.FULL_TIME,
                "fr",
                job.Remote.HYBRID
            ),
            'Ecatepec': scraper.QueryParams (
                "Ecatepec",
                "job_title",
                1.0,
                1 ,
                10 ,
                job.JobType.FULL_TIME,
                "mx",
                job.Remote.OFFICE
            ),
            'Ibadan': scraper.QueryParams (
                "Ibadan",
                "job_title",
                1.0,
                70 ,
                30 ,
                job.JobType.FULL_TIME,
                "ng",
                job.Remote.HYBRID
            ), 
            'MADRID': scraper.QueryParams (
                "MADRID",
                "job_title",
                1.0,
                1 ,
                10 ,
                job.JobType.FULL_TIME,
                "es",
                job.Remote.REMOTE
            ),
            'Qingdao': scraper.QueryParams (
                "Qingdao",
                "job_title",
                1.0,
                1 ,
                10 ,
                job.JobType.FULL_TIME,
                "cn",
                job.Remote.HYBRID

            ),
            'Ufa': scraper.QueryParams (
                "Ufa",
                "job_title",
                1.0,
                1 ,
                10 ,
                job.JobType.FULL_TIME,
                "ru",
                job.Remote.OFFICE
            ),
            'Yangon': scraper.QueryParams (
                "Yangon",
                "job_title",
                1.0,
                1 ,
                10 ,
                job.JobType.FULL_TIME,
                "mm",
                job.Remote.REMOTE
            )

        }

        test_expected = {
            'Abidjan': "https://fr.indeed.com/jobs?q=cleaner&l=Abidjan&radius=25&from=searchOnDesktopSerp",
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