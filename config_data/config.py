from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS')))
        ),
        db=DatabaseConfig(
            db_host=env('DB_HOST'),
            db_port=env('DB_PORT'),
            db_user=env('DB_USER'),
            db_password=env('DB_PASSWORD'),
            database=env('DATABASE')
        )
    )
