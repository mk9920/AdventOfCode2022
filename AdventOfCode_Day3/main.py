import pandas as pd
from Input_1 import alphabets, values
print(alphabets)
print(values)
df = pd.read_excel("Day3_AdventOfCode_Input.xlsx", header=None, names=["Items"])
df["NoOfItems"] = df["Items"].str.len()
Items_1stCompartment = []
Items_2ndCompartment = []
for item in df["Items"]:
    middle_number = int(len(item)/2)
    first_item = item[:middle_number]
    second_item = item[middle_number:]
    Items_1stCompartment.append(first_item)
    Items_2ndCompartment.append(second_item)
df["Items_1stCompartment"] = Items_1stCompartment
df["Items_2ndCompartment"] = Items_2ndCompartment
common = []
for (index, row) in df.iterrows():
# set() method is used to convert any of the iterable to sequence of iterable elements
# with distinct elements, commonly called Set
    c1 = set(df["Items_1stCompartment"][index])
    c2 = set(df["Items_2ndCompartment"][index])
    common.append((c1 & c2))

# where you can't modify how it's created, you can use iterable unpacking like this
#https://stackoverflow.com/questions/53213550/remove-curly-brackets-from-a-list-of-sets-in-python
common = [x for x, in common]
print(type(common))
df['Common'] = common
df['Common'] = df['Common'].astype(str)
df
weight = []
for item in df['Common']:
    c = alphabets.index(item)+1
    weight.append(c)
df["Weight"] = weight
print(sum(df['Weight']))
print("Maulik")
