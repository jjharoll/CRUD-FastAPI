from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.movie_direction import MovieDirection
from config.database import Session
from service.movie_direction import DirectionMovieService

direction_movie_router = APIRouter()

@direction_movie_router.get('/direction',tags=['direction'], response_model=MovieDirection, status_code= 200)
def get_movie_direction() ->MovieDirection:   
    db = Session()
    result = DirectionMovieService(db).get_movie_direction()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)


@direction_movie_router.post('/direction', tags=['direction'], status_code=201 , response_model=dict)
def create_movie_direction(direction:MovieDirection) ->dict:
    db= Session()
    DirectionMovieService(db).create_movie_direction(direction)
    return JSONResponse(content={'message':'direction save in data base'})

@direction_movie_router.put('/direction{id}',tags=['direction'])
def update_movie_direction(id:int,direction:MovieDirection):
    db =  Session
    result = DirectionMovieService(db).update_movie_direction(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    DirectionMovieService(db).update_movie_directon(id,direction)
    return JSONResponse(content={"message":"Se ha modificado la direccion con id: {id}"})

@direction_movie_router.delete('/direction/{id}',tags=['direction'])
def delete_movie_direction(id:int):
        db = Session()
        result = DirectionMovieService(db).delete_movie_direction(id)
        if not result:
            return JSONResponse(status_code=404,content={"message":"No found"})
        return JSONResponse(content="Delete direction", status_code=200)