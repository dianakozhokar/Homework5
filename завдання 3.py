import pandas as pd

input_file = "student_performance.csv"
sort_columns = ["total_score", "grade"]

try:
    df = pd.read_csv(input_file, sep=';', encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(input_file, sep=';', encoding='cp1251')

df.columns = df.columns.str.strip()

print("Назви стовпців:", df.columns.tolist())

data = df.values.tolist()

col_indices = [df.columns.get_loc(col) for col in sort_columns]

for i in range(len(data)):
    min_index = i
    for j in range(i + 1, len(data)):
        for col in col_indices:
            if data[j][col] < data[min_index][col]:
                min_index = j
                break
            elif data[j][col] > data[min_index][col]:
                break
    data[i], data[min_index] = data[min_index], data[i]

df_sorted = pd.DataFrame(data, columns=df.columns)

print("\n=== Відсортовані дані ===")
print(df_sorted)