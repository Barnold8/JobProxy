import scraper
from job import JobSite,QueryParams
from dataclasses import is_dataclass

class URL_Formatter:

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

    def indeed(job_site:JobSite,params:scraper.QueryParams)-> str:
        if isinstance(job_site,int) == False or isinstance(params, QueryParams) == False:
            raise TypeError(f"\n\tjob_site: {type(job_site)}, EXPECTED: int\n\tparams: {type(params)}, EXPECTED: job.QueryParams \n\tJOB: {isinstance(job_site,int)}\n\tPARAMS: {isinstance(params, QueryParams)}")
        
        return f"https://{params.locale}.indeed.com/jobs?q={params.job_title}&l={params.location}&radius={params.radius}&from=searchOnDesktopSerp"

    def reed(job_site:JobSite,params:scraper.QueryParams):
        pass
