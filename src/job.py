from enum import Enum
from dataclasses import dataclass

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
class JobSite:

    INDEED = 1
    REED   = 2
