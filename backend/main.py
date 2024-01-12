from fastapi import FastAPI, HTTPException,Request
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from app.lib.database import crud, models, schemas
from app.lib.database.config import RMD_session
from sqlalchemy.orm import Session
from sqlalchemy import update
import random
import time
app = FastAPI()
load_dotenv()
# add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # which original can access to resouse
    allow_credentials=True, # indicate the browser shoold include cookie or authentication HTTPs
    allow_methods=["*"], # HTTP methods
    allow_headers=["*"], # can be use header
)
# add time measure 
@app.middleware("http")
async def measure_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    response.headers["X-Response-Time"] = "{:.2f}".format((end_time - start_time)* 1000)
    return response

#set router
@app.post("/registerAccount/{phone}/{person_id}/{password}")
def registerAccount(phone,person_id,password,db:Session = RMD_session):
    try:
        checkAvailable = db.query(models.Users).filter(models.Users.phone == phone).first()
        if checkAvailable  :
            raise HTTPException(status_code=409, detail="User already exists")
        db.add(models.Users(
                phone=phone,
                hash_pass = password,
                identification = person_id,
                refreshtoken = 'null'
            ))
        db.commit()
        return {"mes": "success register"}
    except Exception as e:
       raise HTTPException(status_code=300, detail=str(e))

# define the validate form for testing
@app.post("/login")
def login(data: schemas.login, db: Session = RMD_session):
    try:
        checkUser = db.query(models.Users).filter(
            (models.Users.phone == data.phone) & (models.Users.hash_pass == data.hash_pass)
        ).first()
        if checkUser is not None:
            userInfor = db.query(models.person).filter(models.person.person_id == checkUser.identification).first()
            return userInfor
        raise HTTPException(status_code=300, detail="Wrong password")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/dashboard/birthApplicationRegister")
def birthApplication(data: schemas.birthApp, db: Session = RMD_session):
    try:
        husbandCheck = crud.getPerson(db,data.father_id)
        if husbandCheck is None :
            return {"mes":"wrong identification"}
        data.family_id = husbandCheck.family_id if husbandCheck is not None else 123
        crud.insertPerson(db,data)
        db.commit()
        return {"message": "ok"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
@app.post("/dashboard/marriedRegister")
def marriedRegister(data:schemas.marriedRegisFamily, db:Session = RMD_session):
    try:
        print(data.husband_id)
        husbandCheck = crud.getPerson(db,data.husband_id)
        wifeCheck = crud.getPerson(db,data.wife_id)
        # if husbandCheck is None or wifeCheck is None:
        #     return {"message":"husband error person_id, error code = 4xx"}
        checkFamily = db.query(models.family).filter(models.family.family_id== data.family_id).first()
        if checkFamily is None:
            return {"message": " you are not belong to this family "}
        if husbandCheck.family_id == data.family_id or wifeCheck.family_id == data.family_id:
            married_id = random.randint(10000,100000)
            marriedInfor = models.marriedRegister(
                husband_id = data.husband_id,
                wife_id = data.wife_id,
                date_married= data.date_married,
                family_id = data.family_id,
                married_id = married_id
            )
            db.add(marriedInfor)
            db.commit()
            db.refresh(marriedInfor)
            return {"message":"register success"}
        return {"message": " you are not belong to this family "}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/dashboard/lihon/{husband_id}/{wife_id}")
def lihon(husband_id,wife_id, db:Session=RMD_session):
    try:
        getMarried = db.query(models.marriedRegister).filter(
        models.marriedRegister.husband_id == husband_id, 
        models.marriedRegister.wife_id == wife_id ).first()
        if getMarried is not None:
            usedMarriedP = models.usedMarried(
                married_id = getMarried.married_id,
                person_id = getMarried.husband_id,
            )
            db.add(usedMarriedP)
            usedMarriedP = models.usedMarried(
                married_id = getMarried.married_id,
                person_id = getMarried.wife_id,
            )
            db.add(usedMarriedP)
            db.commit()
            return {"message": "sucess"}
        else:
            return {"message": "Not married before"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/family_detail/{family_id}")
def getFamily(family_id, db:Session=RMD_session):
    """ 
    get all information of all member in a family
    """
    try:
        return crud.getFamilys(db,family_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/search/person/{name}")
def searchPerson(name, db:Session=RMD_session):
    try:
        return db.query(models.person).filter(
            models.person.full_name.like(f'%{name}%'),
            ).limit(10).all()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/dashboard/insurance/{person_id}")
def getInsurances(person_id,db:Session=RMD_session):
    try:
        getInsua = db.query(models.insurance).filter(models.insurance.person_id == person_id).all()
        print(getInsua)
        if getInsua == [] or getInsua  is None:
            return {"mes: this user has no insuarance before"}
        return getInsua
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/dashboard/eletricInvoice/{family_id}")
def getInvoices(family_id, db:Session = RMD_session):
    try:
        getElectricInvoice = db.query(models.eletricInvoice).filter(models.eletricInvoice.family_id == family_id).all()
        
        if getElectricInvoice == [] or getElectricInvoice  is None:
            return {"mes: this family do  not register this service before"}
        return getElectricInvoice
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/MarriedList")
def getMarriedList(db:Session = RMD_session):
    try:
        listMari = db.query(models.marriedRegister).filter(models.marriedRegister.husband_id != 0).limit(100).all()
        if not listMari :
            return {"mes":"no data"}
        return listMari
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/family/transform/{person_id}/{new_family_id}/{new_relation}/")
def removeFamily(person_id,new_family_id,new_relation,db:Session=RMD_session):
    try:
        checkNewfamily = db.query(models.family).filter(models.family.family_id == new_family_id).first()
        print(checkNewfamily)
        if checkNewfamily is not None:
            db.execute(
                update(models.person)
                .where(models.person.person_id == person_id)
                .values(family_id=new_family_id, relation_owner_home=new_relation)
            )
            db.commit()
            return {"mes": "success"}
        else:
            return {"mes": "family with family_id={} does not exist".format(new_family_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/family/createNew/{person_id}/{cur_family}")
def createNewFamily(person_id,cur_family,db:Session=RMD_session):
    try:
        getPerson = crud.getPerson(db,person_id)
        print(     getPerson.relation_owner_home != "chủ hộ")
        if (
                getPerson and
                getPerson.family_id == int(cur_family) and
                getPerson.relation_owner_home != "chủ hộ"
            ):
            newfami = models.family(
                family_id = random.randint(1000000,5000000),
                owner_id = person_id,
                num_members = 1
            )
            db.add(newfami)
            db.commit()
            return {"mes":"success"}
        return {"mes" : " some things wrong with your ID or currrent family or you is owner"}
    except Exception as e:
         raise HTTPException(status_code=400, detail=str(e))

@app.get("/search/{person_id}")
def searchByPersonId(person_id, db:Session = RMD_session):
    try:
        getPerson = crud.getPerson(db,personid=person_id)
        if getPerson:
            return getPerson
        return {"mes":"no data"}
    except Exception as e:
        raise HTTPException(status_code=300, detail=str(e))


@app.get("/search/name/{name}")
def searchName(name,db:Session=RMD_session):
    try:
        getPerson = db.query(models.person).filter(models.person.full_name.ilike(f'%{name}%')).limit(10).all()
        if getPerson:
            return getPerson
        return {"mes" : "no-data"}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))


            
            





    

