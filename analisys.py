import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def func(file):
    results = []
    for column in file.columns[1:]:
        count = np.sum(file[column] == 1)
        percent = count / len(file) * 100
        results.append([column, count, round(percent, 1)])
    result = pd.DataFrame(
        results,
        columns=["Функция", "Количество", "Процент"]
    )
    return result.sort_values("Процент", ascending=False)

result = func(pd.read_csv("competitor_data.csv"))
print("Анализ конкурентов:\n", result.to_string(index=False))
plt.bar(result["Функция"], result["Процент"])
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("competitor.png")
plt.show()

result = func(pd.read_csv("survey_data.csv"))
print("\n\nАнализ опроса:\n", result.to_string(index=False))
plt.bar(result["Функция"], result["Процент"])
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("survey.png")
plt.show()