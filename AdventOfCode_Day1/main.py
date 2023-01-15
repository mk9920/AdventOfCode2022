import pandas as pd
df = pd.read_excel("/Users/maulik/Downloads/Book 1.xlsx", header=None)
a = []
net_calories = 0
for (index, row) in df.iterrows():
    if row.isnull()[0]:
        a.append(net_calories)
        net_calories = 0
    else:
        net_calories += row[0]
print(max(a))


