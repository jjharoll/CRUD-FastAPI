from models.movie_genres import MoviesGenres as MoviesGenresModel 

class MoviesGenresService():
    def __init__(self,db) -> None:
        self.db = db
        
    def get_movie_genres (self) -> MoviesGenresModel:
        result = self.db.query(MoviesGenresModel).all()
        return result
    
    def create_movie_genres (self, moviesgenres: MoviesGenresModel):
        new_movie_genres = MoviesGenresModel(
            mov_id = mov.id,
            gen_id = gen.id
        )
        self.db.add(new_moviesgenres)
        self.db.commit()
        return