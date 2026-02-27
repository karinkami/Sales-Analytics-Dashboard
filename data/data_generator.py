import pandas as pd
import numpy as np
from config import settings


def generate_data():
    """Генерация данных"""
    np.random.seed(settings.RANDOM_SEED)

    dates = pd.date_range(
        start=settings.DATA_START_DATE,
        end=settings.DATA_END_DATE,
        freq="D"
    )

    data = []
    for date in dates:
        for category in settings.CATEGORIES:
            # Количество продаж в день
            for _ in range(np.random.randint(5, 20)):
                product = np.random.choice(settings.PRODUCTS[category])

                # Цена зависит от категории
                if category == "Электроника":
                    price = np.random.uniform(1000, 30000)
                elif category == "Одежда":
                    price = np.random.uniform(500, 8000)
                else:
                    price = np.random.uniform(100, 3000)

                quantity = np.random.randint(1, 4)

                data.append({
                    "date": date,
                    "category": category,
                    "product": product,
                    "price": round(price, 2),
                    "quantity": quantity,
                    "revenue": round(price * quantity, 2),
                    "customer_rating": round(np.random.uniform(3.0, 5.0), 1),
                    "city": np.random.choice(settings.CITIES),
                    "payment_method": np.random.choice(settings.PAYMENT_METHODS)
                })

    return pd.DataFrame(data)