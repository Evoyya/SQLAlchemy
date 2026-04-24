from sqlalchemy import select, func, cast, Integer, and_, join
from sqlalchemy.orm import aliased, joinedload, selectinload, contains_eager
from src.Homework_bd_10.database.database_settings import session_factory, engine
from src.Homework_bd_10.database.models import ProductsOrm, ProductLiencesORM, ProductCounts


class SyncORM():
    """
    Синхронные ORM запросы
    """
    @staticmethod
    def select_product_by_id(prodict_id: int):
        with session_factory() as session:
            # Вывод 1 продукта по id
            product = session.get(ProductsOrm, prodict_id)
            print(f'{product=}')


    @staticmethod
    def select_products():
        # Вывод всех продуктов из products
        with session_factory() as session:
            query = select(ProductsOrm) # SELECT * FROM products
            result = session.execute(query)
            products = result.scalars().all()
            print(f'{products=}')


    @staticmethod
    def update_product_price_by_id(product_id: int, new_price: float):
        with session_factory() as session:
            product = session.get(ProductsOrm, product_id)
            if product != None:
                product.price = new_price
                session.flush()
                session.commit()
            else:
                session.refresh().all() # Возращаем значения которые были раньше в БД
                print(f'[Ошибка] товар с id={product_id} не найден!')


    @staticmethod
    def select_products_avg_category(like_category: str, price_low: float = 1000.0):
        """
        Ищет среднюю price по category, групирует по country и отсекает слишком низкие price
        :param like_category: по какой сategory сортируем
        :param price_low: нижняя планка price
        :return: list
        """
        prorm = aliased(ProductsOrm)
        with session_factory() as session:
            engine.echo = False
            query = (
                select(prorm.category,
                       prorm.country,
                       func.avg(prorm.price).cast(Integer).label('avg_price'),
                )
                .where(and_(prorm.category.contains(like_category),
                            prorm.price > price_low,
                            ))
                .group_by(prorm.category, prorm.country)
            )
            #print(query.compile(compile_kwargs={'literal_binds': True})) #Текст запроса, если хочешь посмотреть
            result = session.execute(query).all()
            engine.echo = True
            print(result)
            return result


    @staticmethod
    def selsect_product_id_by_license(license_category: str):
        """
        Возращает id_products+brand по категориям lisence
        :param lisence_category: категория lisence (UER, RU, USA)
        :return: list
        """
        engine.echo = False
        field_name = f'license_{license_category}'
        with session_factory() as session:
            targer_field = getattr(ProductLiencesORM, field_name)
            query = (
                select(ProductLiencesORM.product_id,
                       ProductLiencesORM.brand
                )
                .where(targer_field == True)
            )
            #print(query.compile(compile_kwargs={'literal_binds': True})) #Текст запроса, если хочешь посмотреть
            result = session.execute(query).all()
            engine.echo = True
            print(result)
            return result


    @staticmethod
    def select_product_by_license(license_category: str):
        """
        Возращает обхект класса ProductsORM по категориям lisence, используя selsect_product_id_by_lisence()
        :param lisence_category: категория lisence (UER, RU, USA)
        :return: list
        """
        engine.echo = False
        # Выполнение selsect_product_id_by_lisence()
        select_result = SyncORM.selsect_product_id_by_lisence(license_category)
        product_ids = [row.product_id for row in select_result]
        if not product_ids:
            print(f"Нет товаров с лицензией {license_category}")
            return []

        with session_factory() as session:
            query = (select(ProductsOrm)).where(ProductsOrm.id.in_(product_ids))
            # print(query.compile(compile_kwargs={'literal_binds': True})) #Текст запроса, если хочешь посмотреть
            result = session.execute(query).scalars().all()
            engine.echo = True
            print(result)
            return result


    @staticmethod
    def select_products_joined_by_license(license_category: str):
        """
         Возращает объект класса ProductsORM по категориям lisence, используя join по
         products.id и products_license.product_id
        :param lisence_category: категория lisence (UER, RU, USA)
        :return: list
        """
        engine.echo = False
        field_name = f'license_{license_category}'
        with (session_factory() as session):
            target_field = getattr(ProductLiencesORM, field_name)
            query = select(ProductsOrm
                           ).join(ProductLiencesORM,ProductsOrm.id == ProductLiencesORM.product_id
                                  ).where(target_field == True)

            #print(query.compile(compile_kwargs={'literal_binds': True})) #Текст запроса, если хочешь посмотреть
            result = session.execute(query).scalars().all()
            engine.echo = True
            print(result)
            return result


    @staticmethod
    def select_sum_count_by_product_id(product_id:int):
        """
        Возращает суммарное количество свех product по заданому product_id, находящихся на складе
        группирует по product_id+brand
        :param product_id: product.id
        :return: list
        """
        pc = aliased(ProductCounts) # alias в aql (сокращения)
        with session_factory() as session:
            engine.echo = False
            query =(
                select(pc.product_id,
                       pc.brand,
                       cast(func.sum(pc.count), Integer).label('sum_count'),
                )
                .where(and_(pc.product_id == product_id,
                            pc.date_of_departure == None
                            ))
                .group_by(pc.product_id,pc.brand)
            )
            result = session.execute(query).all()
            #print(query.compile(compile_kwargs={'literal_binds': True})) #Текст запроса, если хочешь посмотреть
            engine.echo = True
            print(result)


    @staticmethod
    def select_all_active_products():
        """
        Возращает все автивные product (находящиеся на складе)
        :return: list
        """
        with session_factory() as session:
            engine.echo = False
            query = select(ProductCounts).where(ProductCounts.date_of_departure == None)
            result = session.execute(query).scalars().all()
            #print(query.compile(compile_kwargs={'literal_binds': True})) #Текст запроса, если хочешь посмотреть
            print(result)
            engine.echo = True

    @staticmethod
    def select_license_with_joined_load_by_product_id(product_id: int):
        """
        Функция подгружает лецензию по product_id для определенного product,
        с помощью releshanships + joinedload
        :param product_id: id product в ProductsOrm
        :return:
        """
        with session_factory() as session:
            engine.echo = False
            query = (
                select(ProductsOrm)
                .options(joinedload(ProductsOrm.product_license))
                .where(ProductsOrm.id == product_id)
            )
            #print(query.compile(compile_kwargs={'literal_binds': True})) #Текст запроса, если хочешь посмотреть
            session.flush()
            result = session.execute(query).scalars().one_or_none()
            if result:
                product_license_by_id = result.product_license
                print(product_license_by_id)
            else:
                print(f'<<Для product_id = {id} нет соотвествующего ProductOrm>>')
            engine.echo = True

    @staticmethod
    def select_license_with_joined_load_by_product_ids(*ids: int):
        """
        Функция подгружает лецензии по product_id для определенных product,
        с помощью releshanships + joinedload
        :return: ProductLiencesORM
        :param idы: id product в ProductsOrm
        """
        with session_factory() as session:
            engine.echo = False
            query = (
                select(ProductsOrm)
                .options(joinedload(ProductsOrm.product_license))
                .where(ProductsOrm.id.in_(ids))
            )
            #print(query.compile(compile_kwargs={'literal_binds': True})) #Текст запроса, если хочешь посмотреть
            session.flush()
            result = session.execute(query).scalars().all()
            for result_id in range(len(ids)):
                try:
                    product_license_by_id = result[result_id].product_license
                    print(product_license_by_id)
                except IndexError:
                    print('<IndexError>')
                    print(f'Для id = {ids[result_id]} нет соотвествующего product_id')
            engine.echo = True


    @staticmethod
    def select_counts_with_select_in_load_by_product_id(product_id: int):
        """
        Возращает все ProductCounts, по id,
        bcgjkmoe. selectinload
        :param product_id: id в ProductORM
        :return: list(*ProductCounts)
        """
        with session_factory() as session:
            engine.echo = False
            query = (
                select(ProductsOrm)
                .options(selectinload(ProductsOrm.product_counts))
                .where(ProductsOrm.id == product_id)
            )
            # print(query.compile(compile_kwargs={'literal_binds': True})) #Текст запроса, если хочешь посмотреть
            result = session.execute(query).scalars().all()
            if result:
                for item in result:
                    product_counts_by_id = item.product_counts
                    for pr in product_counts_by_id:
                        print(pr)
            else:
                print(f'Для такого product_id = {product_id} нет соотвествующего product')

    @staticmethod
    def select_product_with_condition_relationship():
        with session_factory() as session:
            engine.echo = False
            query = (
                select(ProductsOrm)
                .options(selectinload(ProductsOrm.product_counts_active))
            )
            result = session.execute(query).scalars().all()
            for item in result:
                if item.product_counts_active:
                    print(item.product_counts_active)

            engine.echo = True


    @staticmethod
    def select_product_with_condition_relationship_constains_eager():
        with session_factory() as session:
            engine.echo = False
            query = (
                select(ProductsOrm)
                .join(ProductsOrm.product_counts)
                .options(contains_eager(ProductsOrm.product_counts))
                .filter(ProductCounts.date_of_departure == None)
            )
            result = session.execute(query).unique().scalars().all()
            for item in result:
                print(item.product_counts_active)

            engine.echo = True
















