from fastapi import FastAPI
from adapters.db.sqlite_repository import SqliteGameRepository
from adapters.api.routes import create_router
from application.use_cases import GameUseCases

app = FastAPI()

repository = SqliteGameRepository("games.db")
use_cases = GameUseCases(repository)

app.include_router(create_router(use_cases))