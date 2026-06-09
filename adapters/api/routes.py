from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from application.use_cases import GameUseCases

router = APIRouter()

class GameRequest(BaseModel):
    title: str
    genre: str
    platform: str
    rating: float

def create_router(use_cases: GameUseCases) -> APIRouter:

    @router.get("/games")
    def get_all_games():
        return use_cases.get_all_games()

    @router.get("/games/{id}")
    def get_game_by_id(id: int):
        game = use_cases.get_game_by_id(id)
        if not game:
            raise HTTPException(status_code=404, detail="Game not found")
        return game

    @router.post("/games")
    def add_game(request: GameRequest):
        return use_cases.add_game(
            title=request.title,
            genre=request.genre,
            platform=request.platform,
            rating=request.rating
        )

    return router