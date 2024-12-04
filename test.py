import pandas as pd
import pytest
from app import titanic_data

data = {
        "Sex": ["male", "female", "male", "female"],
        "Fare": [10.0, 20.0, 30.0, 40.0]
	}
df = pd.DataFrame(data)

def test_min_fare():
    result = titanic_data(sample_data, "female", "Минимальная цена билета")
    assert result == 20.0

def test_max_fare():
    result = titanic_data(sample_data, "male", "Максимальная цена билета")
    assert result == 30.0

def test_mean_fare():
    result = titanic_data(sample_data, "female", "Средняя цена билета")
    assert result == 30.0

