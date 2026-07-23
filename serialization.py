#to export model

from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pincode: str

class Patient(BaseModel):
    name:str
    age:str
    address: Address

ad = {"city":"Islamabad","state":"Pakhtun Khwa","pincode":"12345"}

pt = {"name":"Yar","age":"12","address":ad}
patient1 = Patient(**pt)

patient1.model_dump() #as dictionary exported
patient1.model_dump_json() #as json exported
 #we can add include and exclude in ()