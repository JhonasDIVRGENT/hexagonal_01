import sqlite3
from typing import List, Optional
from domain.models import Game
from domain.ports import GameRepository

class SqliteGameRepository(GameRepository):

    def __init__(self, db_path: str):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS games (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    platform TEXT NOT NULL,
                    rating REAL NOT NULL
                )
            """)

    def get_all(self) -> List[Game]:
        with sqlite3.connect(self.db_path) as conn:
            rows = conn.execute("SELECT * FROM games").fetchall()
            return [Game(id=r[0], title=r[1], genre=r[2], platform=r[3], rating=r[4]) for r in rows]

    def get_by_id(self, id: int) -> Optional[Game]:
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute("SELECT * FROM games WHERE id = ?", (id,)).fetchone()
            if row:
                return Game(id=row[0], title=row[1], genre=row[2], platform=row[3], rating=row[4])
            return None

    def save(self, game: Game) -> Game:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "INSERT INTO games (title, genre, platform, rating) VALUES (?, ?, ?, ?)",
                (game.title, game.genre, game.platform, game.rating)
            )
            game.id = cursor.lastrowid
            return game