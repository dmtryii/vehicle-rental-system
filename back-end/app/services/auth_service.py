
from datetime import date
import os
from flask_jwt_extended import create_access_token

from app.exceptions.auth_exception import InvalidCredentialsException
from app.extensions import db
from app.exceptions.user_exception import (
    EmptyFieldException,
    InvalidEmailException, 
    PasswordTooShortException, 
    UsernameAllreadyPresentException)
from app.helpers.validation import validate_email
from app.models.users import BaseUser, Gender, Role
from app.services.users_services import check_min_age


def singin(username: str, password: str) -> str:
    if not username:
        raise EmptyFieldException(message='Missing username')
    
    if not password:
        raise EmptyFieldException(message='Missing password')
    
    user = BaseUser.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        raise InvalidCredentialsException()

    return create_access_token(identity=user.id)


def singup(username: str, password: str, email: str,
            first_name: str, last_name: str, 
            gender: Gender, birthday: date) -> str:
    if not username:
        raise EmptyFieldException(message='Username cannot be empty')
        
    if len(password) < 6:
        raise PasswordTooShortException(message='Password must be at least 6 characters long')

    if not first_name or not last_name:
        raise EmptyFieldException(message='First name and last name cannot be empty')
    
    if not validate_email(email):
        raise InvalidEmailException()
    
    user = BaseUser.query.filter_by(username=username).first()
    
    if user:
        raise UsernameAllreadyPresentException()
    
    min_age = int(os.environ.get('MIN_AGE'))
    check_min_age(birthday, min_age)
        
    new_user = BaseUser(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
        birthday=birthday,
        gender=gender
    )
    
    __set_default_role(new_user)
    
    new_user.set_password(password)
        
    db.session.add(new_user)
    db.session.commit()

    return create_access_token(identity=new_user.id)


def __set_default_role(user: BaseUser) -> None:
    role = Role.query.filter_by(name='default').first()

    if not role:
        role = Role(name='default')
        
    user.roles.append(role)
