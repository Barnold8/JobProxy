from typing import List
from backend import scraper
from .job import JobSite,JobType, QueryParams, Remote
from dataclasses import is_dataclass

def space_to_dash(string:str) ->str:
    return string.replace(" ", "-")

def args_have_value(args: List) -> bool:
    for elem in args:
        if elem != None:
            return True
    return False

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
        
        arguments = [params.radius,params.salary_min,params.salary_max]
        url = "https://www.reed.co.uk/jobs/"

        match params.job_type:
            case JobType.FIXED_CONTRACT:
                url += "contract-"
            case JobType.FULL_TIME:
                url += "full-time-"
            case JobType.PART_TIME:
                url += "part-time-"
            case _:
                url += ""

        if params.graduate == True:
            url += "graduate-"

        match params.remote:
            case Remote.HYBRID:
                url += "work-from-home-" # not sure how to handle this case yet since reed doesnt properly support hybrid options
            case Remote.REMOTE:
                url += "work-from-home-"
            case _:
                url += ""

        url += space_to_dash(params.job_title) + "-" if len(params.job_title) > 0 else ""
        url += "jobs-in-" + space_to_dash(params.location) if len(params.location) > 0 else ""
        url += "?" if args_have_value(arguments) else ""

        if params.radius != None:
            url += f"proximity={params.radius}"
        if params.salary_min != None and params.salary_max != None:
            url += f"&salaryFrom={params.salary_min}&salaryTo={params.salary_max}"

        return url


