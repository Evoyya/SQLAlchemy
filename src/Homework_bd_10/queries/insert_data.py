import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.Homework_bd_10.database.database_settings import session_factory, engine
from src.Homework_bd_10.database.models import ProductsOrm, ProductLiencesORM, ProductCounts
from src.Homework_bd_10.queries.data_storage import products_storage, licenses_storage, product_counts_storage


class InsertData():

    @staticmethod
    def insert_data_products(products_storage: list = products_storage):
        """
        Заполняет products данными из products_storage
        :param products_storage: хранилище для products
        :return: None
        """
        engine.echo = False
        with session_factory() as session:
            products_to_add = []
            for item in products_storage:
                product = ProductsOrm(**item)
                products_to_add.append(product)
            session.add_all(products_to_add)
            session.flush() # Отправляем данные в БД до commit
            session.commit()
        engine.echo = True

    @staticmethod
    def insert_data_license(license_storage: list = licenses_storage):
        """
        Заполняет products_license данными из license_storage
        :param license_storage: хранилище для products_license
        :return: None
        """
        engine.echo = False
        with session_factory() as session:
            products_to_add = []
            for item in license_storage:
                pr_license = ProductLiencesORM(**item)
                products_to_add.append(pr_license)
            session.add_all(products_to_add)
            session.flush()
            session.commit()
        engine.echo = True

    @staticmethod
    def insert_data_counts(product_counts_storage=product_counts_storage):
        """
        Заполняет products_counts данными из product_counts_storage
        :param product_counts_storage: хранилище данных для products_counts
        :return: None
        """
        engine.echo = False
        with session_factory() as session:
            product_to_add = []
            for item in product_counts_storage:
                pr_counts = ProductCounts(**item)
                product_to_add.append(pr_counts)
            session.add_all(product_to_add)
            session.flush()
            session.commit()
            engine.echo = True


    @staticmethod
    def insert_all_data():
        """
        Вставляет все данные, вызывая все функции insert
        :return: None
        """
        InsertData.insert_data_products()
        InsertData.insert_data_license()
        InsertData.insert_data_counts()









