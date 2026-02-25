from pydantic import AnyUrl, BaseModel, EmailStr, Field
from typing import List, Annotated

class Patient(BaseModel):
    name : Annotated[str, Field(..., min_length=2, max_length=50, description="Name must be between 2 and 50 characters")] # required field name : str
    email : EmailStr
    linked_in : AnyUrl
    age : int = Field(..., gt=0, description="Age must be a positive integer")
    weight : float
    married : bool # default value married : bool = False
    allergies : List[str] = Field(max_length=8) # optional field allergies : List[str] = []
    contact_info : dict[str, str]



def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted patient data successfully")

patient_info = Patient(name="John Doe", age=30)
insert_patient_data(patient_info)