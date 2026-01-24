import unittest
import src.scraper as scraper
import src.job as job

# Source - https://stackoverflow.com/a
# Posted by pts, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-24, License - CC BY-SA 4.0

if 'unittest.util' in __import__('sys').modules:
    # Show full diff in self.assertEqual.
    __import__('sys').modules['unittest.util']._MAX_LENGTH = 999999999

################################################################################

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
                100000000000000,
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
            ),
        }

        test_expected = {
            'Abidjan':  "https://fr.indeed.com/jobs?q=cleaner&l=Abidjan&radius=10&from=searchOnDesktopSerp",
            'Ecatepec': "https://mx.indeed.com/jobs?q=programmer&l=Ecatepec&radius=-5&from=searchOnDesktopSerp",
            'Ibadan':   "https://ng.indeed.com/jobs?q=politician&l=Ibadan&radius=25&from=searchOnDesktopSerp",
            'MADRID':   "https://es.indeed.com/jobs?q=NOT_A_JOB&l=MADRID&radius=25&from=searchOnDesktopSerp",
            'Qingdao':  "https://cn.indeed.com/jobs?q=\"bricklayer\"&l=Qingdao&radius=25&from=searchOnDesktopSerp",
            'Ufa':      "https://ru.indeed.com/jobs?q=A Weird String © tHat_ h.'/as so-1szme difüüfeürent küinds oüf chaĐracters &l=Ufa&radius=100000000000000&from=searchOnDesktopSerp",
            'Yangon':   "https://mm.indeed.com/jobs?q=&l=Abidjan&radius=25&from=searchOnDesktopSerp",
        }

        for key in test_input.keys():
            self.assertEqual(
                test_expected[key],
                scraper.Scraper.format_site_url(job.JobSite.INDEED,test_input[key])
            )


        assert False

if __name__ == "__main__":
    unittest.main()