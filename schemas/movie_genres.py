from typing import Optional
from pydantic import BaseModel, Field

class MovieGenres(BaseModel):
    mov_id: int
    gen_id: int
    
    class config:
        schema_extra = {
            "example":{
                "mov_id": 1,
                "gen_id": 1
            }
        }