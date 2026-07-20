from fastapi import FastAPI

ap = FastAPI()

def load_data():
  with open ("patients.json", "r") as f:
       data = json.laod()
    return data

@app.get("/view")
def view_all():
  data = load_data()
return data
