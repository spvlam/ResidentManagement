# for checking validation data, can be for input or output passing testing data
from pydantic import BaseModel,conint
from datetime import date

class login(BaseModel):
    phone:str
    hash_pass:str

class userBase(BaseModel):
    phone: int

class userCreate(userBase):
    hash_pass: str
    identification: int
    refreshtoken: str
    # class Config:
    #     from_attributes = True
class persons(BaseModel):
    full_name : str 
    person_id : int 
    que_quan_tinh : str 
    que_quan_huyen : str 
    que_quan_xa : str 
    family_id : int
    dob : date
    gender : str
    relation_owner_home : str 
    father_id : int
    mother_id : int
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "birth_id": 12345,
    #             "full_name": "John Doe",
    #             "person_id": 67890,
    #             "que_quan_tinh": "Some Province",
    #             "que_quan_huyen": "Some District",
    #             "que_quan_xa": "Some Commune",
    #             "family_id": 54321,
    #             "dob": "1990-01-01",
    #             "gender": "Male",
    #             "father_id":2003,
    #             "mother_id":2004,
    #             "hopital":"bachmai",
    #             "relation_owner_home": "child",
    #             "married_status": "Single",

    #         }
    #     }

# birth applicatioin
class birthApp(persons):
    hopital : str

class marriedRegisFamily(BaseModel):
    husband_id : int
    wife_id :int 
    date_married : date
    family_id: int


class lihon(BaseModel):
    husband_id : int
    wife_id :int 

