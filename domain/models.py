from dataclasses import dataclass
@dataclass
class Game : 
    id : int
    title : str
    genre : str
    platform : str
    rating : float 