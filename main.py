from fastapi import FastAPI,HTTPException,Path
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

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)