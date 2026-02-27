import pandas as pd


def filter_data(df, date_range, categories, cities, min_rating):
    """Применение фильтров"""
    filtered = df.copy()

    start_date, end_date = date_range
    filtered = filtered[
        (filtered["date"].dt.date >= start_date) &
        (filtered["date"].dt.date <= end_date)
        ]

    filtered = filtered[filtered["category"].isin(categories)]
    filtered = filtered[filtered["city"].isin(cities)]
    filtered = filtered[filtered["customer_rating"] >= min_rating]

    return filtered


def calculate_kpi(df):
    """Расчет показателей"""
    if df.empty:
        return {
            "total_revenue": 0,
            "avg_check": 0,
            "total_sales": 0,
            "avg_rating": 0,
            "avg_quantity": 0,
            "unique_products": 0,
            "unique_categories": 0
        }

    return {
        "total_revenue": df["revenue"].sum(),
        "avg_check": df["revenue"].mean(),
        "total_sales": len(df),
        "avg_rating": df["customer_rating"].mean(),
        "avg_quantity": df["quantity"].mean(),
        "unique_products": df["product"].nunique(),
        "unique_categories": df["category"].nunique()
    }