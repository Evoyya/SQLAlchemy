import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.Homework_bd_10.queries.create_tables import create_products_table
from src.Homework_bd_10.queries.insert_data import InsertData
from src.Homework_bd_10.queries.queries import SyncORM

create_products_table() # Создание таблицы
InsertData.insert_all_data()

#SyncORM.select_product_by_id(2) # Вызов на печать продукта с id=2
#SyncORM.select_products() # Вызов на печать всех продуктов

# Изменение цены товара по id
#SyncORM.update_product_price_by_id(2, 15500)

#SyncORM.select_products_avg_category('Phones')

#SyncORM.selsect_product_id_by_license('RU')

#SyncORM.select_product_by_license('RU')

#SyncORM.select_products_joined_by_license('RU')

#SyncORM.select_sum_count_by_product_id(1)

#SyncORM.select_all_active_products()

#SyncORM.select_license_with_joined_load_by_product_id(2)

#SyncORM.select_license_with_joined_load_by_product_ids(2,3,5,80)

#SyncORM.select_counts_with_select_in_load_by_product_id(7)

SyncORM.select_product_with_condition_relationship()
print('-'*150)
SyncORM.select_product_with_condition_relationship_constains_eager()