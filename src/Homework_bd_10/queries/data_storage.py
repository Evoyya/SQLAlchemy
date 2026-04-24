from datetime import date

# Список словарей с данными для таблицы products
products_storage = [
    {
        "brand": "Loreal", "price": 5000, "country": "France", "category": "Cosmetics",
        "production_date": date(2023, 1, 1), "delivery_date": date(2023, 1, 11)
    },
    {
        "brand": "Chanel", "price": 15000, "country": "France", "category": "Perfume",
        "production_date": date(2023, 1, 1), "delivery_date": date(2023, 1, 21)
    },
    {
        "brand": "Mishuk", "price": 5000, "country": "China", "category": "Electronics",
        "production_date": date(2023, 5, 1), "delivery_date": date(2023, 5, 10)
    },
    {
        "brand": "QueenBee", "price": 12000, "country": "USA", "category": "Honey",
        "production_date": date(2022, 8, 1), "delivery_date": date(2022, 8, 5)
    },
    {
        "brand": "WonderBra", "price": 8000, "country": "USA", "category": "Clothing",
        "production_date": date(2022, 9, 1), "delivery_date": date(2022, 9, 5)
    },
    {
        "brand": "Nokia", "price": 3000, "country": "Finland", "category": "Phones",
        "production_date": date(2020, 5, 10), "delivery_date": date(2020, 5, 25)
    },
    {
        "brand": "Samsung", "price": 25000, "country": "Korea", "category": "Phones",
        "production_date": date(2020, 5, 28), "delivery_date": date(2020, 6, 2)
    },
    # Этот товар для теста: первая цифра года '5', марка заканчивается на 's'
    {
        "brand": "Adidas", "price": 7000, "country": "Germany", "category": "Shoes",
        "production_date": date(5025, 1, 1), "delivery_date": date(5025, 2, 1)
    },
    {
        "brand": "Lays", "price": 100, "country": "USA", "category": "Food",
        "production_date": date(2023, 1, 1), "delivery_date": date(2023, 1, 2)
    },
    {
        "brand": "Samsung", "price": 12000, "country": "Korea", "category": "Phones",
        "production_date": date(2023, 1, 1), "delivery_date": date(2023, 1, 2)
    },
    {
        "brand": "Samsung", "price": 800, "country": "Korea", "category": "Phones",
        "production_date": date(2023, 1, 1), "delivery_date": date(2023, 1, 2)
    }
]

licenses_storage = [
    {"product_id": 1,  "brand": "Loreal",    "license_EUR": True,  "license_RU": True,  "license_USA": True},
    {"product_id": 2,  "brand": "Chanel",    "license_EUR": True,  "license_RU": False, "license_USA": True},
    {"product_id": 3,  "brand": "Mishuk",    "license_EUR": False, "license_RU": True,  "license_USA": False},
    {"product_id": 4,  "brand": "QueenBee",  "license_EUR": False, "license_RU": False, "license_USA": True},
    {"product_id": 5,  "brand": "WonderBra", "license_EUR": True,  "license_RU": True,  "license_USA": True},
    {"product_id": 6,  "brand": "Nokia",     "license_EUR": True,  "license_RU": True,  "license_USA": False},
    {"product_id": 7,  "brand": "Samsung",   "license_EUR": True,  "license_RU": True,  "license_USA": True},
    {"product_id": 8,  "brand": "Adidas",    "license_EUR": True,  "license_RU": True,  "license_USA": True},
    {"product_id": 9,  "brand": "Lays",      "license_EUR": False, "license_RU": True,  "license_USA": True},
    {"product_id": 10, "brand": "Samsung",   "license_EUR": True,  "license_RU": True,  "license_USA": True},
    {"product_id": 11, "brand": "Samsung",   "license_EUR": True,  "license_RU": True,  "license_USA": True},
]

product_counts_storage = [
    # --- Товар ID 1: Loreal ---
    # 1. Старая поставка (уехала)
    {
        "product_id": 1,
        "brand": "Loreal",
        "count": 100,
        "date_of_receipt": date(2023, 1, 10),
        "date_of_departure": date(2023, 2, 1)
    },
    # 2. Новая поставка (лежит)
    {
        "product_id": 1,
        "brand": "Loreal",
        "count": 50,
        "date_of_receipt": date(2023, 5, 20),
        "date_of_departure": None
    },

    # --- Товар ID 7: Samsung (Флагман) ---
    # 3. Январская партия (ушла)
    {
        "product_id": 7,
        "brand": "Samsung",
        "count": 10,
        "date_of_receipt": date(2023, 1, 5),
        "date_of_departure": date(2023, 1, 15)
    },
    # 4. Февральская партия (ушла)
    {
        "product_id": 7,
        "brand": "Samsung",
        "count": 20,
        "date_of_receipt": date(2023, 2, 1),
        "date_of_departure": date(2023, 2, 20)
    },
    # 5. Мартовская партия (лежит)
    {
        "product_id": 7,
        "brand": "Samsung",
        "count": 15,
        "date_of_receipt": date(2023, 3, 10),
        "date_of_departure": None
    },
    # 6. Свежая летняя партия (лежит)
    {
        "product_id": 7,
        "brand": "Samsung",
        "count": 5,
        "date_of_receipt": date(2023, 6, 1),
        "date_of_departure": None
    },

    # --- Товар ID 9: Lays (Чипсы) ---
    # 7. Огромная партия (быстро съели)
    {
        "product_id": 9,
        "brand": "Lays",
        "count": 10000,
        "date_of_receipt": date(2023, 1, 1),
        "date_of_departure": date(2023, 1, 5)
    },
    # 8. Еще одна партия (лежит)
    {
        "product_id": 9,
        "brand": "Lays",
        "count": 5000,
        "date_of_receipt": date(2023, 6, 1),
        "date_of_departure": None
    },

    # --- Товар ID 3: Mishuk ---
    # 9. Неликвид (лежит с начала года)
    {
        "product_id": 3,
        "brand": "Mishuk",
        "count": 1000,
        "date_of_receipt": date(2023, 1, 1),
        "date_of_departure": None
    },

    # --- Товар ID 6: Nokia ---
    # 10. Транзитная партия (пришла и ушла в один день)
    {
        "product_id": 6,
        "brand": "Nokia",
        "count": 50,
        "date_of_receipt": date(2023, 2, 1),
        "date_of_departure": date(2023, 2, 1)
    },
    # 11. Еще одна партия (лежит)
    {
        "product_id": 6,
        "brand": "Nokia",
        "count": 60,
        "date_of_receipt": date(2023, 4, 1),
        "date_of_departure": None
    },
]