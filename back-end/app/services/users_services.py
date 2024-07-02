
from typing import List
from datetime import date

from app.helpers import converters 
from app.models.users import BaseUser
from app.exceptions.user_exception import InvalidAgeException


def get_all() -> List:
    return BaseUser.query.all()

        
def check_min_age(birthday: str, min_age: int) -> None:
    birthday = converters.str_to_date(birthday)
    
    today = date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    if age < min_age:
        raise InvalidAgeException(f'User must be at least {min_age} years old')
        