from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, and_
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    email = Column(String, primary_key=True)
    password = Column(String)
    firstName = Column(String)
    lastName = Column(String)

    def to_response(self):
        return {
            "email": self.email,
            "firstName": self.firstName,
            "lastName": self.lastName
        }

    def to_payload(self):
        return {
            "email": self.email,
            "password": self.password
        }

class Database:
    def __init__(self):
        engine = create_engine("postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/postgres")
        # un-comment to ease testing
        # Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)

    def add_user(self, user_dict):
        s = self.session()
        s.add(User(**user_dict))
        s.commit()
        s.close()

    def verify_user(self, user_cred):
        s = self.session()
        r = s.query(User).filter(and_(User.email==user_cred["email"], User.password==user_cred["password"])).first()
        user_cred = r.to_payload()
        s.commit()
        s.close()      
        return  user_cred

    def update_user(self, user_cred, new_user):
        s = self.session()
        r = s.query(User).filter(and_(User.email==user_cred["email"], User.password==user_cred["password"])).first()
        r.firstName = new_user["firstName"]
        r.lastName = new_user["lastName"]
        s.add(r)
        s.commit()
        s.close()       

    def get_all_users(self):
        s = self.session()
        r = s.query(User).all()
        all_users = [x.to_response() for x in r]
        s.commit()
        s.close() 
        return all_users                  

    