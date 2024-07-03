
from enum import Enum


class Gender(Enum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'

    def __str__(self):
        return self.value
    

class Status(Enum):
    AVAILABLE = 'AVAILABLE'
    RENTED_OUT = 'RENTED_OUT'
    UNDER_MAINTENANCE = 'UNDER_MAINTENANCE'

    def __str__(self):
        return self.value
    