from sqlalchemy import Column, Integer, String, Float ,Date, MetaData
from .config import Base

metadata = MetaData()  # for handling these case without primary key
class Users(Base):
    __tablename__ = "users"
    identification = Column(Integer, primary_key=True, index=True)
    phone = Column(String, unique=True)
    hash_pass = Column(String)
    refreshtoken = Column(String)

class person(Base):
    __tablename__ ="person"
    full_name = Column(String)
    person_id = Column(Integer, index=True, primary_key= True)
    que_quan_tinh = Column(String,)
    que_quan_huyen = Column(String)
    que_quan_xa = Column(String)
    family_id = Column(Integer)
    dob = Column(Date)
    gender = Column(String)
    relation_owner_home = Column(String)
    married_status = Column(String)
    father_id = Column(Integer)
    mother_id = Column(Integer)

class usedMarried(Base):
    __tablename__ = "used_to_married"
    married_id = Column(Integer, primary_key= True)
    person_id = Column(Integer , index= True)

class marriedRegister(Base):
    __tablename__="married_register"
    husband_id = Column(Integer)
    wife_id = Column(Integer)
    married_id = Column(Integer,primary_key=True)
    date_married = Column(Date)
    family_id = Column(Integer)

class family(Base):
    __tablename__="family"
    family_id = Column(Integer,primary_key=True)
    owner_id = Column(Integer)
    num_members = Column(Integer)

class insurance(Base):
    __tablename__="insurance"
    person_id = Column(Integer)
    insurance_id = Column(Integer, primary_key= True)
    price = Column(Float)
    insurance_name = Column(String)

class eletricInvoice(Base):
    __tablename__="electric_info"
    electric_id = Column(Integer, primary_key= True)
    family_id = Column(Integer)
    price = Column(Integer)
    curr_day = Column(Date)


class UsedFamily(Base):
    __tablename__ = 'used_to_belong_family'
    id = Column(Integer, primary_key=True, autoincrement=True)
    person_id = Column(Integer)
    relation_old_person = Column(String)
    old_family = Column(Integer)
    