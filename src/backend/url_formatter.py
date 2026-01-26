from backend import scraper
from .job import JobSite,JobType, QueryParams
from dataclasses import is_dataclass

class URL_Formatter:

    @staticmethod
    def format_url(job_site:JobSite,params:scraper.QueryParams):
        
        match job_site:
            case JobSite.INDEED:
                return URL_Formatter.indeed(
                    job_site,params
                )
            case JobSite.REED:
                return URL_Formatter.reed(
                    job_site,params
                )        

    @staticmethod
    def indeed(job_site:JobSite,params:QueryParams)-> str:
        return f"https://{params.locale}.indeed.com/jobs?q={params.job_title}&l={params.location}&radius={params.radius}&from=searchOnDesktopSerp"

    @staticmethod
    def reed(job_site:JobSite,params:QueryParams)-> str:
         # https://www.reed.co.uk/jobs/{job-type}-{work-from-home (if remote)}-{job}-jobs-in-{location}?proximity={radius}&salaryFrom={aalarymin}&salaryTo={salarymax}  
        
        url = "https://www.reed.co.uk/jobs/"

        match params.job_type:

            case JobType.GRADUATE:
                url += "graduate-"
            case JobType.FIXED_CONTRACT:
                url += "contract-"
            case JobType.FULL_TIME:
                url += "full-time-"
            case JobType.PART_TIME:
                url += "part-time-"
            case _:
                url += ""

        return url


