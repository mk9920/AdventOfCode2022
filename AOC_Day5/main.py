import pandas as pd
# Read a table of fixed-width formatted lines into DataFrame.
df = pd.read_fwf("input_1.txt", header=None)
df_reverse = df.iloc[::-1]
dict1 = df_reverse.to_dict(orient='Series')

# https://stackoverflow.com/questions/75195397/modifying-input-data-to-a-usable-list-format-using-python/75195564#75195564

L = [v.str.strip('[]').dropna().tolist() for k, v in dict1.items()]
df1 = pd.read_fwf("input.txt", header=None)[9:]
df1 = df1.iloc[:, 0].str.split(" ", expand=True)
df1 = df1.drop(df.columns[[0, 2, 4]], axis=1)
for (index, row) in df1.iterrows():
    item_moved = int(row.iloc[0])
    from_list = int(row.iloc[1])-1
    to_list = int(row.iloc[2])-1
    # Sol1:
    # moved_items = L[from_list][:-item_moved-1:-1]
    # L[to_list] = L[to_list] + moved_items
    # L[from_list] = L[from_list][:-item_moved]

    #Sol2
    moved_items = L[from_list][-item_moved:]
    L[to_list] = L[to_list] + moved_items
    L[from_list] = L[from_list][:-item_moved]
a = []
for item in range(len(L)):
    a.append(L[item][-1])
b = ""
for item in a:
    b += item
print(a)
print(b)


