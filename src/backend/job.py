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

    pass

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