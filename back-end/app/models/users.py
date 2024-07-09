
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

from app.extensions import db, bcrypt
from app.models.rentals import user_discount
from app.helpers.enums import Gender


user_role = db.Table(
    'users_roles', 
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True)
)


class User(db.Model, SerializerMixin):    
    __tablename__ = 'users'
    
    # Primary Key
    id = db.Column(db.Integer, primary_key=True)
    
    # User credentials
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    
    # User status
    is_active = db.Column(db.Boolean(), default=True)
    
    # Personal details
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    
    birthday = db.Column(db.Date, nullable=False)
    
    # Registration date
    registration = db.Column(db.DateTime, default=datetime.now, nullable=False)
    
    roles = db.relationship('Role', secondary=user_role, back_populates='users')
    
    rentals = db.relationship('Rental', back_populates='user')
    
    discounts = db.relationship('Discount', secondary=user_discount, back_populates='users')
    
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
    
    serialize_rules = ('-password_hash', '-roles.users', '-rentals.user', '-discounts.users')
       
    
class Role(db.Model, SerializerMixin):
    __tablename__ = 'roles'
        
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    
    users = db.relationship('User', secondary=user_role, back_populates='roles')
    
    serialize_rules = ('-users.roles',)
