import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def show_revenue_by_category(df):
    """Выручка по категориям"""
    data = df.groupby("category")["revenue"].sum().reset_index()

    fig = px.bar(
        data,
        x="category",
        y="revenue",
        color="revenue",
        color_continuous_scale="Blues",
        text_auto=".0s",
        title="Выручка по категориям"
    )

    fig.update_layout(
        xaxis_title="",
        yaxis_title="Рубли",
        height=350,
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)


def show_city_distribution(df):
    """Продажи по городам"""
    data = df.groupby("city")["revenue"].sum().reset_index()

    fig = px.pie(
        data,
        values="revenue",
        names="city",
        title="Доля продаж по городам",
        hole=0.3
    )

    fig.update_layout(height=350)
    fig.update_traces(textposition="inside", textinfo="percent+label")

    st.plotly_chart(fig, use_container_width=True)


def show_sales_trend(df):
    """Динамика продаж"""
    data = df.groupby("date")["revenue"].sum().reset_index()

    fig = px.line(
        data,
        x="date",
        y="revenue",
        title="Динамика продаж",
        markers=True
    )

    fig.update_layout(
        xaxis_title="Дата",
        yaxis_title="Выручка (₽)",
        height=350
    )

    st.plotly_chart(fig, use_container_width=True)


def show_payment_methods(df):
    """Способы оплаты"""
    data = df["payment_method"].value_counts().reset_index()
    data.columns = ["method", "count"]

    fig = px.bar(
        data,
        x="method",
        y="count",
        color="method",
        text_auto=True,
        title="Способы оплаты"
    )

    fig.update_layout(
        xaxis_title="",
        yaxis_title="Количество",
        height=350,
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)


def show_top_products(df):
    """Топ товаров"""
    data = df.groupby("product")["revenue"].sum().nlargest(5).reset_index()

    fig = px.bar(
        data,
        x="revenue",
        y="product",
        orientation="h",
        color="revenue",
        color_continuous_scale="Greens",
        text_auto=".0s",
        title="Топ-5 товаров по выручке"
    )

    fig.update_layout(
        xaxis_title="Выручка (₽)",
        yaxis_title="",
        height=300
    )

    st.plotly_chart(fig, use_container_width=True)


def show_rating_distribution(df):
    """Распределение рейтингов"""
    fig = px.histogram(
        df,
        x="customer_rating",
        nbins=10,
        title="Распределение оценок",
        color_discrete_sequence=["#1976d2"]
    )

    fig.update_layout(
        xaxis_title="Рейтинг",
        yaxis_title="Количество",
        height=300
    )

    st.plotly_chart(fig, use_container_width=True)


def show_recent_sales(df):
    """Последние продажи"""
    data = df[["date", "category", "product", "city", "revenue"]].head(10).copy()
    data["date"] = data["date"].dt.strftime("%d.%m.%Y")
    data.columns = ["Дата", "Категория", "Товар", "Город", "Выручка"]

    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Выручка": st.column_config.NumberColumn(format="%.0f ₽")
        }
    )