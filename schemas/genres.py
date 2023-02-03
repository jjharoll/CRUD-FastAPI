from typing import Optional
from pydantic import BaseModel, Field

class Genres(BaseModel):
    gen_id: Optional[int] = None
    gen_title: str = Field(max_lenght = 15, min_lenght= 1)
    
    class config:
        schema_extra = {
            "example":{
                "gen_id": 1,
                "gen_title": "Action"
            }
        }