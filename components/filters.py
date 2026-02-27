import streamlit as st
from datetime import datetime


def render_filters(df):
    """Понятные фильтры в боковой панели"""
    with st.sidebar:
        st.header("⚙️ Параметры")

        # Дата
        st.subheader("📅 Период")
        min_date = df["date"].min().date()
        max_date = df["date"].max().date()

        start_date = st.date_input(
            "С",
            value=min_date,
            min_value=min_date,
            max_value=max_date
        )

        end_date = st.date_input(
            "По",
            value=max_date,
            min_value=min_date,
            max_value=max_date
        )

        date_range = (start_date, end_date)

        st.divider()

        # Категории
        st.subheader("📦 Категории")
        all_cats = st.checkbox("Все категории", value=True)

        if all_cats:
            categories = df["category"].unique()
            st.caption(f"Выбрано: {len(categories)}")
        else:
            categories = st.multiselect(
                "Выберите категории",
                options=df["category"].unique(),
                default=df["category"].unique()[:2]
            )

        st.divider()

        # Города
        st.subheader("🏙️ Города")
        all_cities = st.checkbox("Все города", value=True)

        if all_cities:
            cities = df["city"].unique()
            st.caption(f"Выбрано: {len(cities)}")
        else:
            cities = st.multiselect(
                "Выберите города",
                options=df["city"].unique(),
                default=df["city"].unique()[:2]
            )

        st.divider()

        # Рейтинг
        st.subheader("⭐ Рейтинг")
        min_rating = st.slider(
            "Минимальный рейтинг",
            min_value=0.0,
            max_value=5.0,
            value=3.0,
            step=0.5
        )

        # Кнопки
        col1, col2 = st.columns(2)
        with col1:
            apply_btn = st.button("✅ Применить", use_container_width=True)
        with col2:
            reset_btn = st.button("🔄 Сбросить", use_container_width=True)

            if reset_btn:
                st.rerun()

        # Инфо
        st.divider()
        st.info(f"""
        **О данных:**
        - Записей: {len(df):,}
        - Категорий: {df['category'].nunique()}
        - Городов: {df['city'].nunique()}
        """)

    return date_range, categories, cities, min_rating