from fastapi import FastAPI,HTTPException,Path,Query
from pydantic import BaseModel,computed_field,Field
from typing import Literal,Annotated
from fastapi.responses import JSONResponse
import uvicorn
import json

app = FastAPI()


class Patient(BaseModel):
    id: Annotated[str,Field(...,description="Patient ID in DB",examples=["P001"])]
    name:Annotated[str,Field(...,description="Patient Name")]
    city:Annotated[str,Field(...,description="Patient City")]
    age: Annotated[int,Field(...,gt=0,lt=120,description="Patient Age")]
    gender:Annotated[str,Literal['male','female','others'],Field(...,description="Patient Gender")]
    height:Annotated[float,Field(...,description="Patient Height in meters")]
    weight:Annotated[float,Field(...,description="Patient Weight in kg")]

    @computed_field()
    @property
    def bmi(self)->float:
        bmi = self.weight / (self.height ** 2)
        return bmi

    @computed_field()
    @property
    def verdict(self)->str:
        if self.bmi < 18.5:
            return 'underweight'
        elif self.bmi < 25:
            return 'overweight'
        elif self.bmi < 30:
            return 'obese'
        else:
            return "healthy"



def load_data():
  with open ("patients.json", "r") as f:
    data = json.load(f)
    return data

def write_data(data):
    with open ("patients.json","w") as f:
        json.dump(data,f)

#to see all patients data
@app.get("/view")
def view_all():
    data = load_data()
    return data


#to see specific patient data
@app.get("/patient/{patient_id}")
def get_patient(patient_id: str = Path(...,description="Patient ID in DB",example="P001")):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    return data[patient_id]


#
@app.get("/sort")
def sort_patients(sort_by: str = Query(...,description="Sort by height,weight or bmi",),order:str = Query('asc',description="sort by ascending or descending order")):
    data = load_data()
    valid_fields= ["height","weight","bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=404, detail="Wrong option,Sort by height or weight or bmi.")
    if order not in ["asc","desc"]:
        raise HTTPException(status_code=404, detail="order can be ascending or descending")

    sort_order = False if order == "asc" else True
    sorted_data= sorted(data.values(), key=lambda x:x.get(sort_by,0),reverse=sort_order)
    return sorted_data


@app.post("/create")
def create_Patient(patient: Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")

    else:
        data[patient.id] = patient.model_dump(exclude=['id'])
        write_data(data)

    return JSONResponse(status_code=201,content={"message":"Patient created successfully"})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)