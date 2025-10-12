import pandas as pd

data = pd.read_csv("insurance.csv")

bubble_sorted = data.values.tolist()
charges_index = list(data.columns).index("charges")


n = len(bubble_sorted)
for i in range(n):
    for j in range(0, n - i - 1):
        if bubble_sorted[j][charges_index] > bubble_sorted[j + 1][charges_index]:

            bubble_sorted[j], bubble_sorted[j + 1] = bubble_sorted[j + 1], bubble_sorted[j]


sorted_data = pd.DataFrame(bubble_sorted, columns=data.columns)

print(sorted_data)

