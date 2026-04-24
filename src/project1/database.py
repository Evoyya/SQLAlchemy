from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, text
from config import setting
import asyncio
#from models import metadata_obj

sync_engine = create_engine(
    url=setting.DATABASE_URL_psycopg,
    echo=True, # все запросы отобращаются в консоли True
    pool_size=5, # макс количество подключений
    max_overflow=10 # количество дополнительный подключений
)

async_engine = create_async_engine(
    url=setting.DATABASE_URL_asyncpg,
    echo=True, # все запросы отобращаются в консоли True
)

# Объявление сессий
session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

class Base(DeclarativeBase):
    pass
    #metadata = metadata_obj



