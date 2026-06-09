from abc import ABC , abstractmethod
from typing import List , Optional 
from domain.models import Game

class GameRepository(ABC):
    @abstractmethod
    def get_all (self)-> List [Game]:
        pass
    @abstractmethod
    def get_by_id (self, id : int) -> Optional [Game]:
        pass
    @abstractmethod
    def  save (self, game :Game) -> Game :
        pass