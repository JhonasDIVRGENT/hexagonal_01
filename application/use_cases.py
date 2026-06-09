from typing import List , Optional
from domain.models import Game
from domain.ports import GameRepository

class GameUseCases:
    def __init__ (self , repository : GameRepository):
        self.repository = repository
        
    def get_all_games (self) -> List [Game]:
        return self.repository.get_all ()
    
    def get_game_by_id (self , id: int )-> Optional [Game]:
        return self.repository.get_by_id (id)
    
    def add_game (self , title:str , genre: str , platform:str , rating : float) ->Game:
        game=Game (id=0 , title =title , genre = genre , platform = platform, rating= rating)
        return self.repository.save (game)
        
