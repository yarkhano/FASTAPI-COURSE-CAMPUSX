from pydantic import BaseModel
from typing import List,Dict,Optional

class Patient(BaseModel):
    name: str
    age: int
    allergies: Optional[List[str]] = None
    contact: Dict[str,str]

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.contact)


a = {
    'name': 'Yar Khan',
    'age': 22,
    'allergies': ['bronchi'],

    'contact': {
        'email': 'yar@gmail',
        'phone': '03456787659'
    }
}
patient1 = Patient(**a)
insert_patient(patient1)
