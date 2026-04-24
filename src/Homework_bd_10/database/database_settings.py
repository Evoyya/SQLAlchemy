from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from pydantic_settings import BaseSettings

DB_USER = "postgres"       # Ваше имя пользователя (обычно postgres)
DB_PASS = "5640"           # Ваш пароль от Postgres
DB_HOST = "localhost"      # Адрес (localhost, если база на вашем пк)
DB_PORT = "5432"           # Порт (стандартный 5432)
DB_NAME = "Test2_SQLAlchemy"    # Имя базы данных (ОНА ДОЛЖНА УЖЕ СУЩЕСТВОВАТЬ!)

class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432  # Можно использовать int
    DB_USER: str = "postgres"  # Исправил опечатку (было DB_URER)
    DB_PASS: str = "5640"
    DB_NAME: str = "Test2_SQLAlchemy"

    @property
    def DATABASE_URL_psycopg(self):
        return f'postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

settings = Settings()



engine = create_engine(url=settings.DATABASE_URL_psycopg,
                       echo=True
                       )
session_factory = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    repr_cols_num = 7
    repr_cols = tuple()
    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"

