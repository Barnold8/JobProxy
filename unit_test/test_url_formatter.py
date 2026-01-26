import unittest
import backend.scraper as scraper
import backend.url_formatter as url_formatter
import backend.job as job

# Source - https://stackoverflow.com/a
# Posted by pts, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-24, License - CC BY-SA 4.0

if 'unittest.util' in __import__('sys').modules:
    # Show full diff in self.assertEqual.
    __import__('sys').modules['unittest.util']._MAX_LENGTH = 999999999

################################################################################

class Test_URL_Formatter(unittest.TestCase):

    test_input = {
        'Abidjan': scraper.QueryParams (
            "Abidjan",
            "cleaner",
            -10,
            1 ,
            10 ,
            job.JobType.PART_TIME,
            "fr",
            job.Remote.HYBRID,
            False
        ),
        'Ecatepec': scraper.QueryParams (
            "Ecatepec",
            "programmer",
            -5,
            1 ,
            10 ,
            job.JobType.APPRENTICESHIP,
            "mx",
            job.Remote.OFFICE,
            False
        ),
        'Ibadan': scraper.QueryParams (
            "Ibadan",
            "politician",
            25,
            70 ,
            30 ,
            job.JobType.FULL_TIME,
            "ng",
            job.Remote.HYBRID,
            True
        ), 
        'MADRID': scraper.QueryParams (
            "MADRID",
            "NOT_A_JOB",
            2147483647,
            1 ,
            10 ,
            job.JobType.INTERNSHIP,
            "es",
            job.Remote.REMOTE,
            False
        ),
        'Qingdao': scraper.QueryParams (
            "Qingdao",
            "\"bricklayer\"",
            9,
            1 ,
            10 ,
            job.JobType.PERMANENT,
            "cn",
            job.Remote.HYBRID,
            False

        ),
        'Ufa': scraper.QueryParams (
            "Ufa",
            "A Weird String © tHat_ h.'/as so-1szme difüüfeürent küinds oüf chaĐracters ",
            100000000000000,
            1 ,
            10,
            job.JobType.FULL_TIME,
            "ru",
            job.Remote.OFFICE,
            False
        ),
        'Yangon': scraper.QueryParams (
            "Yangon",
            "",
            25,
            1 ,
            10 ,
            job.JobType.FIXED_CONTRACT,
            "mm",
            job.Remote.REMOTE,
            False
        ),
        'Edinburg'   : None,
        'Hamburg'    : -1,
        "Riscani"    : "ff",
        "Moen"       : False,
        "Magtanggol" : 8.0
    }

    def test_space_to_dash(self):
        pass
    def test_args_have_value(self):
        pass

    def test_parse_site(self):
        pass

    def test_format_site_url_INDEED(self):
        
        test_input = Test_URL_Formatter.test_input
        test_expected = {
            'Abidjan':  "https://fr.indeed.com/jobs?q=cleaner&l=Abidjan&radius=-10&from=searchOnDesktopSerp",
            'Ecatepec': "https://mx.indeed.com/jobs?q=programmer&l=Ecatepec&radius=-5&from=searchOnDesktopSerp",
            'Ibadan':   "https://ng.indeed.com/jobs?q=politician&l=Ibadan&radius=25&from=searchOnDesktopSerp",
            'MADRID':   "https://es.indeed.com/jobs?q=NOT_A_JOB&l=MADRID&radius=2147483647&from=searchOnDesktopSerp",
            'Qingdao':  "https://cn.indeed.com/jobs?q=\"bricklayer\"&l=Qingdao&radius=9&from=searchOnDesktopSerp",
            'Ufa':      "https://ru.indeed.com/jobs?q=A Weird String © tHat_ h.'/as so-1szme difüüfeürent küinds oüf chaĐracters &l=Ufa&radius=100000000000000&from=searchOnDesktopSerp",
            'Yangon':   "https://mm.indeed.com/jobs?q=&l=Yangon&radius=25&from=searchOnDesktopSerp",
        }

        test_unexpected = [
            'Edinburg',
            'Hamburg',
        ]

        ## Check valid instances 
        for key in test_expected.keys():
            self.assertEqual(
                test_expected[key],
                url_formatter.URL_Formatter.indeed(job.JobSite.INDEED,test_input[key])
            )

        ## Check invalid instances
        for key in test_unexpected:
            self.assertRaises(
                AttributeError,
                url_formatter.URL_Formatter.indeed,
                job.JobSite.INDEED,
                test_input[key]
            )

    def test_format_site_url_REED(self):
        # https://www.reed.co.uk/jobs/{job-type}-{work-from-home (if remote)}-{job}-jobs-in-{location}?proximity={radius}&salaryFrom={aalarymin}&salaryTo={salarymax}  
       
        test_input = Test_URL_Formatter.test_input
        test_expected = {
            'Abidjan':  "https://www.reed.co.uk/jobs/part-time-work-from-home-cleaner-jobs-in-Abidjan?proximity=-10&salaryFrom=1&salaryTo=10",
            'Ecatepec': "https://www.reed.co.uk/jobs/programmer-jobs-in-Ecatepec?proximity=-5&salaryFrom=1&salaryTo=10",
            'Ibadan':   "https://www.reed.co.uk/jobs/full-time-graduate-work-from-home-politician-jobs-in-Ibadan?proximity=25&salaryFrom=70&salaryTo=30",
            'MADRID':   "https://www.reed.co.uk/jobs/work-from-home-NOT_A_JOB-jobs-in-MADRID?proximity=2147483647&salaryFrom=1&salaryTo=10",
            'Qingdao':  "https://www.reed.co.uk/jobs/work-from-home-\"bricklayer\"-jobs-in-Qingdao?proximity=9&salaryFrom=1&salaryTo=10",
            'Ufa':      "https://www.reed.co.uk/jobs/full-time-A-Weird-String-©-tHat_-h.'/as-so-1szme-difüüfeürent-küinds-oüf-chaĐracters--jobs-in-Ufa?proximity=100000000000000&salaryFrom=1&salaryTo=10",
            'Yangon':   "https://www.reed.co.uk/jobs/contract-work-from-home-jobs-in-Yangon?proximity=25&salaryFrom=1&salaryTo=10",
        }

        test_unexpected = [
            'Edinburg',
            'Hamburg',
        ]

        ## Check valid instances 
        for key in test_expected.keys():
            self.assertEqual(
                test_expected[key],
                url_formatter.URL_Formatter.reed(job.JobSite.INDEED,test_input[key])
            )

        ## Check invalid instances
        for key in test_unexpected:
            self.assertRaises(
                AttributeError,
                url_formatter.URL_Formatter.reed,
                job.JobSite.REED,
                test_input[key]
            )