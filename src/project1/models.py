from database import Base
from sqlalchemy.orm import Mapped, mapped_column


""" 
# Императивный стиль
metadata_obj = MetaData()

workers_table = Table(
    'workers',
    metadata_obj,
    Column('id' , Integer, primary_key=True),
    Column('username' , String),
)
"""

# Декларативный стиль
class WorkersOrm(Base):
    __tablename__ = 'workers'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]

#metadata_obj = MetaData()
