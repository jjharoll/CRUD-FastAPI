from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.genres import Genres
from config.database import Session
from service.genres import GenresService


genres_router = APIRouter()

@genres_router.get('/genres',tags=['genres'], response_model=Genres, status_code= 200)
def get_genres() ->Genres:   
    db = Session()
    result = GenresService(db).get_genres()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)


@genres_router.post('/genres', tags=['genres'], status_code=201 , response_model=dict)
def create_genres(genres:Genres) ->dict:
    db= Session()
    GenresService(db).create_genres(genres)
    return JSONResponse(content={'message':'genres save in data base'})

@genres_router.put('/genres{id}',tags=['genres'])
def update_genres(id:int,genres:Genres):
    db =  Session
    result = GenresService(db).get_genres(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    GenresService(db).update_genres(id,genres)
    return JSONResponse(content={"message":"Se ha modificado el genres con id: {id}"})

@genres_router.delete('/genres/{id}',tags=['genres'])
def delete_genres(id:int):
        db = Session()
        result = GenresService(db).get_genres(id)
        if not result:
            return JSONResponse(status_code=404,content={"message":"No found"})
        GenresService(db).delete_genres(id)
        return JSONResponse(content="Delete genres", status_code=200)