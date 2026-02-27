import streamlit as st
from config import settings
from data import data_generator
from components import filters, metrics, charts
from utils import helpers

# Настройка страницы
st.set_page_config(
    page_title=settings.DASHBOARD_TITLE,
    layout=settings.DASHBOARD_LAYOUT
)

# Простой CSS
st.markdown("""
<style>
    .main-header {
        background: #1976d2;
        color: white;
        padding: 1rem;
        border-radius: 5px;
        margin-bottom: 1rem;
    }
    .block-container {
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Заголовок
st.markdown('<div class="main-header"><h1>📊 Анализ продаж</h1></div>',
            unsafe_allow_html=True)

# Загрузка данных
@st.cache_data
def load_data():
    return data_generator.generate_data()

df = load_data()

# Фильтры
date_range, categories, cities, min_rating = filters.render_filters(df)

# Применение фильтров
filtered_df = helpers.filter_data(df, date_range, categories, cities, min_rating)

# Проверка на пустые данные
if filtered_df.empty:
    st.warning("⚠️ Нет данных за выбранный период. Измените параметры фильтрации.")
    st.stop()

# Метрики
st.subheader("📈 Основные показатели")
metrics.render_metrics(filtered_df)

# Первая строка графиков
st.subheader("📊 Анализ продаж")

col1, col2 = st.columns(2)

with col1:
    with st.container():
        charts.show_revenue_by_category(filtered_df)

with col2:
    with st.container():
        charts.show_city_distribution(filtered_df)

# Вторая строка
col1, col2 = st.columns(2)

with col1:
    with st.container():
        charts.show_sales_trend(filtered_df)

with col2:
    with st.container():
        charts.show_payment_methods(filtered_df)

# Третья строка
st.subheader("🏆 Детальный анализ")

col1, col2 = st.columns(2)

with col1:
    with st.container():
        charts.show_top_products(filtered_df)

with col2:
    with st.container():
        charts.show_rating_distribution(filtered_df)

# Таблица с данными
st.subheader("📋 Последние продажи")
charts.show_recent_sales(filtered_df)

# Футер
st.divider()
st.caption("© 2024 - Дашборд анализа продаж")