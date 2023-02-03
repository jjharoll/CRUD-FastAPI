from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import Optional
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field

from models.rating import Rating as RatingModel
from schemas.rating import Rating
from config.database import Session
from service.rating import RatingService


rating_router = APIRouter()

@rating_router.get('/rating',tags=['rating'], response_model=Rating, status_code= 200)
def get_rating() ->Rating:   
    db = Session()
    result = RatingService(db).get_rating()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)


@rating_router.post('/rating', tags=['rating'], status_code=201 , response_model=dict)
def create_rating(rating:Rating) ->dict:
    db= Session()
    RatingService(db).create_rating(rating)
    return JSONResponse(content={'message':'director save in data base'})

@rating_router.put('/rating{id}',tags=['rating'])
def update_rating(id:int,rating:Rating):
    db =  Session
    result = RatingService(db).get_rating(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    RatingService(db).update_rating(id,rating)
    return JSONResponse(content={"message":"Se ha modificado el rating con id: {id}"})

@rating_router.delete('/rating/{id}',tags=['rating'])
def delete_rating(id:int):
        db = Session()
        result = RatingService(db).delete_rating()
        if not result:
            return JSONResponse(status_code=404,content={"message":"No found"})
        return JSONResponse(content="Delete rating", status_code=200)