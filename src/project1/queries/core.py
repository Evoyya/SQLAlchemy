from sqlalchemy import text, insert
from src.project1.database import sync_engine, async_engine
#from src.models import metadata_obj, workers_table

# синхронный вариант
with sync_engine.connect() as conn:
    result = conn.execute(text('SELECT VERSION()')) # Важно оборачивать запросы в text()
    print(f'{result.first()}') # возращает только первую строку
'''
with sync_engine.connect() as conn:
    result = conn.execute(text('SELECT 1,2,3'))
    print(f'{result}')
'''
# асинхронный фариант
async def get_VERSION():
    async with async_engine.connect() as conn:
        result = await conn.execute(text('SELECT VERSION()')) # Важно оборачивать запросы в text()
        print(f'{result.first()}') # возращает только первую строку

def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine) # удаляем все таблицы
    metadata_obj.create_all(sync_engine) # создаём таблицы
    sync_engine.echo = True

def insert_data():
    with sync_engine.connect() as conn:
        # Cпособ похуже
        #stmt = """INSERT INTO workers (username) VALUES
        #        ('Anton Shcheglov'),
        #        ('Arina Fomicheva');"""
        # Способ получше
        stmt = insert(workers_table).values(
            [
                {'username': 'Anton Shcheglov'},
                {'username': 'Arina Fomicheva'},
            ]
        )

        conn.execute(stmt)
        conn.commit()

