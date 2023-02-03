from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.movie_genres import MovieGenres
from config.database import Session
from service.movie_genres import MoviesGenresService


movie_genres_router = APIRouter()

@movie_genres_router.get('/moviegenres',tags=['moviegenres'], response_model=MovieGenres, status_code= 200)
def get_movie_genres() ->MovieGenres:   
    db = Session()
    result = MoviesGenresService(db).get_movie_genres()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)


@movie_genres_router.post('/moviegenres', tags=['moviegenres'], status_code=201 , response_model=dict)
def create_movie_genres(moviegenres:MovieGenres) ->dict:
    db= Session()
    MovieGenresService(db).create_movie_genres(MovieGenres)
    return JSONResponse(content={'message':'movie genre save in data base'})

@movie_genres_router.put('/moviegenres{id}',tags=['moviegenres'])
def update_movie_genres(id:int,moviegenres:MovieGenres):
    db =  Session
    result = MovieGenresService(db).update_movie_genres(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    MoviesGenresService(db).update_movie_genres(id,MovieGenres)
    return JSONResponse(content={"message":"Se ha modificado el movie genre con id: {id}"})

@movie_genres_router.delete('/moviegenres/{id}',tags=['moviegenres'])
def delete_movie_genres(id:int):
        db = Session()
        result = MoviesGenresService(db).delete_movie_genres(id)
        if not result:
            return JSONResponse(status_code=404,content={"message":"No found"})
        return JSONResponse(content="Delete movie genre", status_code=200)