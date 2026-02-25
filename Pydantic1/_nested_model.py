from pydantic import BaseModel, Field,AnyUrl, EmailStr  
from typing import List, Annotated

class Address(BaseModel):
    street : str
    city : str
    state : str
    country : str

class Patient(BaseModel):
    name : Annotated[str, Field(..., min_length=2, max_length=50, description="Name must be between 2 and 50 characters")] # required field name : str
    email : EmailStr
    linked_in : AnyUrl
    age : int = Field(..., gt=0, description="Age must be a positive integer")
    weight : float
    married : bool # default value married : bool = False
    allergies : List[str] = Field(max_length=8) # optional field allergies : List[str] = []
    contact_info : dict[str, str]
    address : Address

patient_info = Patient(name="John Doe", age=30, address=Address(street="123 Main St", city="New York", state="NY", country="USA"))  
print(patient_info)

address_dic = {
    "street": "123 Main St",
    "city": "New York",
    "state": "NY",  
    "country": "USA"
}
patient_info = Patient(name="John Doe", age=30, address=address_dic)
print(patient_info) 
    