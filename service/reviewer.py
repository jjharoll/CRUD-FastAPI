from models.reviewer import Reviewer as ReviewerModel

class ReviewerService():
    def __init__(self,db) -> None:
        self.db = db
        
    def get_reviewer (self) -> ReviewerModel:
        result = self.db.query(ReviewerModel).all()
        return result
    
    def create_reviewer (self, reviewer: ReviewerModel):
        new_reviewer = ReviewerModel(
            rev_id = rev.id,
            rev_name = rev.name
        )
        self.db.add(new_reviewer)
        self.db.commit()
        return
        
    