from scraper import QueryParams
from job import JobSite

class URL_Formatter:

    def format_url(job_site:JobSite,params:QueryParams):

        match job_site:
            case JobSite.INDEED:
                return URL_Formatter.indeed(
                    job_site,params
                )
            case JobSite.REED:
                return URL_Formatter.reed(
                    job_site,params
                )        

    def indeed(job_site:JobSite,params:QueryParams)-> str:
        pass

    def reed(job_site:JobSite,params:QueryParams):
        pass
