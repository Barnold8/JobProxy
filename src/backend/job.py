from enum import Enum
from dataclasses import dataclass

class JobType(Enum):

    FULL_TIME       = 1
    PART_TIME       = 2
    PERMANENT       = 3
    FIXED_CONTRACT  = 4
    INTERNSHIP      = 5
    APPRENTICESHIP  = 6
    FREELANCE       = 7

class Remote(Enum):

    REMOTE = 1
    HYBRID = 2
    OFFICE = 3

class JobSite(Enum):

    INDEED = 1
    REED   = 2

@dataclass
class JobSiteDetails:

    job_card_id   : str
    job_title_id  : str
    job_salary    : str
    job_location  : str
    job_poster    : str
    job_posted_on : str

@dataclass
class Job:
    # Use CSS selector to grab custom attributes and not classnames
    job_title    : str 
    job_salary   : str 
    job_location : str 
    job_time     : str 


@dataclass
class QueryParams:
    location   : str
    job_title  : str
    radius     : float
    salary_min : int
    salary_max : int
    job_type   : JobType
    locale     : str
    remote     : Remote
    graduate   : bool

# Need a method to load these on boot and not hardcode values, allows user to change IDs/ClassNames/CSS_Selector when needed and doesnt need to change codebase
REED_INSTANCE = JobSiteDetails(

    job_card_id   = "index-module_jobCard__body__vWzBf",
    job_title_id  = ".index-module_jobResultHeading__title__r7Yqg",
    job_salary    = "[data-qa=\"job-metadata-salary]\"",
    job_location  = None,
    job_poster    = None,
    job_posted_on = None

)