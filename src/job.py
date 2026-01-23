from dataclasses import dataclass
from enum import Enum

class JobType(Enum):

    FULLTIME        = 1
    PARTTIME        = 2
    PERMANENT       = 3
    FIXEDCONTRACT   = 4
    GRADUATE        = 5
    INTERNSHIP      = 6
    APPRENTICESHIP  = 7
    FREELANCE       = 8

    
@dataclass
class QueryParams:
    location   : str
    job_title  : str
    radius     : float
    salary_min : int
    salary_max : int
    job_type   : JobType