import pandas as pd
import numpy as np

file = pd.read_csv("competitor_data.csv")
results = []
for column in file.columns[1:]:
    count = np.sum(file[column] == 1)
    percent = count / len(file) * 100
    results.append([column, count, round(percent, 1)])
result = pd.DataFrame(
    results,
    columns=["Функция", "Количество", "Процент"]
)
result = result.sort_values("Процент", ascending=False)
print("Анализ конкурентов:\n", result.to_string(index=False))


file = pd.read_csv("survey_data.csv")
results = []
for column in file.columns[1:]:
    count = np.sum(file[column] == 1)
    percent = count / len(file) * 100
    results.append([column, count, round(percent, 1)])
result = pd.DataFrame(
    results,
    columns=["Функция", "Количество", "Процент"]
)
result = result.sort_values("Процент", ascending=False)
print("\n\nАнализ опроса:\n", result.to_string(index=False))