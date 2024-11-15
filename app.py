import pandas as pd
import streamlit as st

# Загрузка данных
@st.cache
def load_data():
    return pd.read_csv("titanic_train.csv")

data = load_data()

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

# Фильтрация данных по полу
filtered_data = data[data['Sex'] == gender]

# Применение выбранной функции
if operation == "Минимальная цена билета":
    result = filtered_data['Fare'].min()
elif operation == "Максимальная цена билета":
    result = filtered_data['Fare'].max()
elif operation == "Средняя цена билета":
    result = filtered_data['Fare'].mean()

# Отображение результата
st.write(f"Результат для {gender}:")
st.table(pd.DataFrame({"Функция": [operation], "Значение": [round(result, 2)]}))