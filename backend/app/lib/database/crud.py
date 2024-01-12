from sqlalchemy.orm import Session
from .models import Users, person,family
from app.lib.database.config import RMD_session
import random
from typing import Optional

db:Session = RMD_session

def get_user(phone:int,db:Session)->Users :
    return db.query(Users).filter(Users.phone == phone).first()

def insertPerson(db:Session,data:person):
    married = "độc thân"
    new_person = person(
    full_name=data.full_name,
    person_id=random.randint(1000000, 5000000),
    que_quan_tinh=data.que_quan_tinh,
    que_quan_huyen=data.que_quan_huyen,
    que_quan_xa=data.que_quan_xa,
    family_id=data.family_id,
    dob=data.dob,
    gender=data.gender,
    relation_owner_home=data.relation_owner_home,
    married_status=married,
    father_id = data.father_id,
    mother_id=data.mother_id
)
    db.add(new_person)

def getPerson(db:Session,personid):
    return db.query(person).filter( person.person_id == personid).first()

def getFamilys(db:Session,family_id):
    return db.query(person).filter(person.family_id == family_id).limit(10).all()
    