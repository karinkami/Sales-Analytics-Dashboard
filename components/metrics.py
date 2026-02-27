import streamlit as st
from utils import helpers


def render_metrics(df):
    """Понятные метрики"""
    kpi = helpers.calculate_kpi(df)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "💰 Выручка",
            f"{kpi['total_revenue']:,.0f} ₽",
            f"{kpi['total_sales']} продаж"
        )

    with col2:
        st.metric(
            "🧾 Средний чек",
            f"{kpi['avg_check']:,.0f} ₽",
            f"{kpi['avg_quantity']:.1f} товаров"
        )

    with col3:
        st.metric(
            "📊 Продажи",
            f"{kpi['total_sales']:,}",
            f"⭐ {kpi['avg_rating']:.1f}"
        )

    with col4:
        st.metric(
            "📦 Товаров",
            f"{kpi['unique_products']}",
            f"{kpi['unique_categories']} категорий"
        )