from src.project1.database import sync_engine, session_factory
from src.project1.models import WorkersOrm #, metadata_obj


def create_tables():
    sync_engine.echo = False
    WorkersOrm.metadata.drop_all(sync_engine) # удаляем все таблицы
    WorkersOrm.metadata.create_all(sync_engine) # создаём таблицы
    sync_engine.echo = True


def insert_data():
    with session_factory() as session:
        worker_0 = WorkersOrm(username='Anton Shcheglov')
        worker_1 = WorkersOrm(username='Arina Fomicheva')
        session.add_all([worker_0, worker_1])
        session.commit()

""" 
async def insert_data():
    async with async_session_factory() as session:
        worker_0 = WorkersOrm(username='Anton Shcheglov')
        worker_1 = WorkersOrm(username='Arina Fomicheva')
        session.add_all([worker_0, worker_1])
        await session.commit()
"""