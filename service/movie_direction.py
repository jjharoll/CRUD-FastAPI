from models.movie_direction import Direction as DirectionModel 

class DirectionMovieService():
    def __init__(self,db) -> None:
        self.db = db
        
    def get_direction_movie (self) -> DirectionModel:
        result = self.db.query(DirectionModel).all()
        return result
    
    def create_direction_movie (self, direction: DirectionModel):
        new_direction = DirectionModel(
            dir_id = director.id,
            mov_id = mov.id,
        )
        self.db.add(new_direction)
        self.db.commit()
        return
        