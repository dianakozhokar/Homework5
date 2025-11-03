import pandas as pd

data = pd.read_csv("student_performance.csv", sep=";", encoding="utf-8")

column_to_sort = "total_score"

if column_to_sort not in data.columns:
    print(f"Стовпець '{column_to_sort}' не знайдено. Доступні стовпці:")
    print(list(data.columns))
    exit()


selection_sorted = data.values.tolist()
col_index = list(data.columns).index(column_to_sort)

n = len(selection_sorted)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if selection_sorted[j][col_index] < selection_sorted[min_index][col_index]:
            min_index = j
    selection_sorted[i], selection_sorted[min_index] = selection_sorted[min_index], selection_sorted[i]

sorted_data = pd.DataFrame(selection_sorted, columns=data.columns)

print(sorted_data.head)
print(sorted_data.head)
