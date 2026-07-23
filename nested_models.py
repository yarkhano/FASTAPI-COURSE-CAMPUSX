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

print(patient1.name)
print(patient1.age)
print(patient1.address.city)
