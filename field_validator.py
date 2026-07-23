from pydantic import BaseModel,EmailStr,AnyUrl,Field,Annotated,field_validator
from typing import List,Dict,Optional


class Patient(BaseModel):
    name: str
    age: int = Field(gt=0,lt=120)
    email: EmailStr
    weight:float
    linkedin_url: AnyUrl
    allergies: Optional[List[str]]
    contact: Dict[str,str]



#field_validator use for custom validation like an email will contain a specific str like after @ buic
#by default mode is = after which mean first data coercion is occured than value is passed to the class and vicer versa when mode=before

@field_validator("email")
@classmethod
def val_email(cls,value):
    valid_names = ["buic","buik"]
    domain_name = value.split("@")[-1]
    if domain_name not in valid_names:
        raise ValueError(f"Invalid email address {value}")
    return value



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
