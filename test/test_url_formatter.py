import unittest
import src.scraper as scraper
import src.url_formatter as url_formatter
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
                "programmer",
                -5,
                1 ,
                10 ,
                job.JobType.FULL_TIME,
                "mx",
                job.Remote.OFFICE
            ),
            'Ibadan': scraper.QueryParams (
                "Ibadan",
                "politician",
                25,
                70 ,
                30 ,
                job.JobType.FULL_TIME,
                "ng",
                job.Remote.HYBRID
            ), 
            'MADRID': scraper.QueryParams (
                "MADRID",
                "NOT_A_JOB",
                2147483647,
                1 ,
                10 ,
                job.JobType.FULL_TIME,
                "es",
                job.Remote.REMOTE
            ),
            'Qingdao': scraper.QueryParams (
                "Qingdao",
                "\"bricklayer\"",
                9,
                1 ,
                10 ,
                job.JobType.FULL_TIME,
                "cn",
                job.Remote.HYBRID

            ),
            'Ufa': scraper.QueryParams (
                "Ufa",
                "A Weird String © tHat_ h.'/as so-1szme difüüfeürent küinds oüf chaĐracters ",
                100000000000000,
                1 ,
                10,
                job.JobType.FULL_TIME,
                "ru",
                job.Remote.OFFICE
            ),
            'Yangon': scraper.QueryParams (
                "Yangon",
                "",
                25,
                1 ,
                10 ,
                job.JobType.FULL_TIME,
                "mm",
                job.Remote.REMOTE
            ),
            'Edinburg': None,
            'Hamburg': -1
        }

        test_expected = {
            'Abidjan':  "https://fr.indeed.com/jobs?q=cleaner&l=Abidjan&radius=-10&from=searchOnDesktopSerp",
            'Ecatepec': "https://mx.indeed.com/jobs?q=programmer&l=Ecatepec&radius=-5&from=searchOnDesktopSerp",
            'Ibadan':   "https://ng.indeed.com/jobs?q=politician&l=Ibadan&radius=25&from=searchOnDesktopSerp",
            'MADRID':   "https://es.indeed.com/jobs?q=NOT_A_JOB&l=MADRID&radius=2147483647&from=searchOnDesktopSerp",
            'Qingdao':  "https://cn.indeed.com/jobs?q=\"bricklayer\"&l=Qingdao&radius=9&from=searchOnDesktopSerp",
            'Ufa':      "https://ru.indeed.com/jobs?q=A Weird String © tHat_ h.'/as so-1szme difüüfeürent küinds oüf chaĐracters &l=Ufa&radius=100000000000000&from=searchOnDesktopSerp",
            'Yangon':   "https://mm.indeed.com/jobs?q=&l=Yangon&radius=25&from=searchOnDesktopSerp",
        }

        test_unexpected = {
            'Edinburg': "",
            'Hamburg' : ""
        }

        for key in test_expected.keys():
            self.assertEqual(
                test_expected[key],
                url_formatter.URL_Formatter.indeed(job.JobSite.INDEED,test_input[key])
            )
        

if __name__ == "__main__":
    unittest.main()