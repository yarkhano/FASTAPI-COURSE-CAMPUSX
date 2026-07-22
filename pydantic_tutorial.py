from pydantic import BaseModel,EmailStr,AnyUrl,Field,Annotated
from typing import List,Dict,Optional


class Patient(BaseModel):
    name: str
    age: int = Field(gt=0,lt=120)
    email: EmailStr
    weight:Annotated[float,Field(gt=0,strict=True)] #striict ensure value must be string if =True
    linkedin_url: AnyUrl
    allergies: Annotated[Optional[List[str]],Field(default=None,max_length=5)]
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





#type validation->mean the assurance of the type of the data
#data validation->mean the assurance of the data
