from typing import Optional
from pydantic import BaseModel, Field

class Director(BaseModel):
    id: Optional[int] = None
    dir_fname: str
    dir_lname: str
    
    class config:
        schema_extra = {
            "example":{
                "id": 1,
                "dir_fname": "Vin",
                "dir_fname": "Diesel"
            }
        }