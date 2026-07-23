from pydantic import BaseModel,AnyUrl,Field,model_validator
from typing import List,Dict,Optional,Annotated


class Patient(BaseModel):
    name: str
    age: int = Field(gt=0,lt=120)
    email: str
    weight:float
    linkedin_url: AnyUrl
    allergies: Optional[List[str]]
    contact: Dict[str,str]



#model_validator use for custom validation of multiple fields
#by default mode is = after which mean first data coercion is occured than value is passed to the class and vicer versa when mode=before

    @model_validator(mode='after')
    def val_email(self):
        if self.age > 60 and 'emergency' not in self.contact:
            raise ValueError("Person having age more than 60 require an emergency contact")
        return self



def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.contact)


a = {
    'name': 'Yar Khan',
    'age': 22,
    'email':'yar@buic.com',
    'weight': 60.5,
    'allergies': ['bronchi'],
    'linkedin_url':'https://linkdin.com',
    'contact': {
        'phone': '03456787659',
        'emergency':'4567765'
    }
}
patient1 = Patient(**a)
insert_patient(patient1)
