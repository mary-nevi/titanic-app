import pandas as pd
import streamlit as st

@st.cache
def load_data():
    return pd.read_csv("titanic_train.csv")

data = load_data()

# Функция для вычисления результата
def calculate_fare_stat(data, gender, operation):
    """
    Фильтрует данные по полу и рассчитывает указанную статистику по тарифам.

    :param data: DataFrame с данными Титаника.
    :param gender: Пол ("male" или "female").
    :param operation: Операция ("Минимальная цена билета", "Максимальная цена билета", "Средняя цена билета").
    :return: Вычисленное значение.
    """
    filtered_data = data[data['Sex'] == gender]

    if operation == "Минимальная цена билета":
        return filtered_data['Fare'].min()
    elif operation == "Максимальная цена билета":
        return filtered_data['Fare'].max()
    elif operation == "Средняя цена билета":
        return filtered_data['Fare'].mean()
    else:
        raise ValueError("Неправильная операция.")

# Заголовок приложения
st.title("Анализ данных Титаника")
st.write("Набор данных:")
st.dataframe(data.head())

# Элементы управления
gender = st.radio("Выберите пол:", ["male", "female"])
operation = st.selectbox(
    "Выберите функцию:",
    ["Минимальная цена билета", "Максимальная цена билета", "Средняя цена билета"]
)


result = calculate_fare_stat(data, gender, operation)


st.write(f"Результат для {gender}:")
st.table(pd.DataFrame({"Функция": [operation], "Значение": [round(result, 2)]}))
