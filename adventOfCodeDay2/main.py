import pandas as pd
df = pd.read_excel(r"/Users/maulik/Downloads/Day 2.xlsx", header=None, names=["text"])
df[["OP", "YP"]] = df['text'].str.split(expand=True)
selection_score = []
for item in df['YP']:
    if item == 'X':
        selection_score.append(1)
    elif item == 'Y':
        selection_score.append(2)
    elif item == 'Z':
        selection_score.append(3)
df['Selection_Score'] = selection_score
print("Maulik")


def compare(oc ,yc):
    if (oc == 'A' and yc == 'X') or (oc == 'B' and yc == 'Y') or (oc == 'C' and yc == 'Z'):
        score = 3
        return score
    elif oc == 'A' and yc == 'Y':
        score = 6
        return score
    elif oc == 'A' and yc == 'Z':
        score = 0
        return score
    elif oc == 'B' and yc == 'X':
        score = 0
        return score
    elif oc == 'B' and yc == 'Z':
        score = 6
        return score
    elif oc == 'C' and yc == 'X':
        score = 6
        return score
    elif oc == 'C' and yc == 'Y':
        score = 0
        return score

second_score= []
for (index, row) in df.iterrows():
    temp_scr = compare(df["OP"][index], df["YP"][index])
    second_score.append(temp_scr)

df['second_score'] = second_score
df['total_score'] = df['Selection_Score'] + df['second_score']

print(sum(df['total_score']))
print('Maulik')