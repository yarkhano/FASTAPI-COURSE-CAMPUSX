from fastapi import FastAPI,HTTPException,Path,Query
import json
import uvicorn

app = FastAPI()

def load_data():
  with open ("patients.json", "r") as f:
    data = json.load(f)
    return data

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



    sort_order = True if order == "asc" else False
    sorted_data= sorted(data.values(), key=lambda x:x.get(sort_by,0),reverse=sort_order)
    return sorted_data


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)