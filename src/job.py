from enum import Enum
from dataclasses import dataclass

class JobType(Enum):

    FULL_TIME       = 1
    PART_TIME       = 2
    PERMANENT       = 3
    FIXED_CONTRACT  = 4
    GRADUATE        = 5
    INTERNSHIP      = 6
    APPRENTICESHIP  = 7
    FREELANCE       = 8

@dataclass
class JobSite:

    INDEED_UK = 1
    INDEED_US = 2
    REED   = 3
