from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, ForeignKey, Index, CheckConstraint
from datetime import date
from src.Homework_bd_10.database.database_settings import Base
from typing import Annotated

# Создание переиспользуемых типов столбцов
intpk = Annotated[int, mapped_column(primary_key=True)]
table_date = Annotated[date, mapped_column(Date)]
product_id_fk = Annotated[int, mapped_column(ForeignKey('products.id'), onupdate='CASCADE')]
product_id_pk_fk = Annotated[int, mapped_column(ForeignKey('products.id', onupdate='CASCADE'), primary_key=True)]



# Table products
class ProductsOrm(Base):
    __tablename__ = 'products'
    """
    Table products
    PK = id
    """

    id: Mapped[intpk]

    brand: Mapped[str]
    price: Mapped[float]
    country: Mapped[str]
    category: Mapped[str]
    production_date: Mapped[table_date]
    delivery_date: Mapped[table_date]

    product_license: Mapped['ProductLiencesORM'] = relationship(
        back_populates='product'
    )

    product_counts: Mapped[list['ProductCounts']] = relationship()

    product_counts_active: Mapped[list['ProductCounts']] = relationship(
        primaryjoin="and_(ProductsOrm.id == ProductCounts.product_id, ProductCounts.date_of_departure == None)",
        #lazy='selectin',

    )

    __table_args__ = (
        Index('brand_index', 'brand'),
        CheckConstraint()
    )



class ProductLiencesORM(Base):
    __tablename__ = 'products_license'
    """
    Table liense for products 
    PK = FK = product_id_pk_fk
    """

    product_id: Mapped[product_id_pk_fk]

    brand: Mapped[str]
    license_EUR: Mapped[bool]
    license_RU: Mapped[bool]
    license_USA: Mapped[bool]

    product: Mapped['ProductsOrm'] = relationship(
        back_populates='product_license'
    )

    repr_cols_num = 5


class ProductCounts(Base):
    __tablename__ = 'product_counts'
    """
    Table counts for products 
    PK = id
    FK = product_id 
    """
    id: Mapped[intpk]
    product_id: Mapped[product_id_fk]
    brand: Mapped[str]
    count: Mapped[int]
    date_of_receipt: Mapped[table_date]
    date_of_departure: Mapped[table_date | None]

    repr_cols_num = 6


