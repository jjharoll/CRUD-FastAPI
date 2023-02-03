from models.genres import Genres as GenresModel 

class GenresService():
    def __init__(self,db) -> None:
        self.db = db
        
    def get_genres (self) -> GenresModel:
        result = self.db.query(GenresModel).all()
        return result
    
    def get_genres_id (self, id:int):
        result = self.db.query(GenresModel).filter(GenresModel.id == id).first()
        return result 
    
    def create_genres (self, genres: GenresModel):
        new_genres = GenresModel(
            gen_id = gen.id,
            gen_title = gen.title
        )
        self.db.add(new_genres)
        self.db.commit()
        return
    
        def delete_genres(self,id:int):
            self.db.query(GenresModel).filter(GenresModel.id == id).delete()
            self.db.commit()
            return