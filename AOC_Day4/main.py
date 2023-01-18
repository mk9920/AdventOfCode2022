import pandas as pd
df = pd.read_excel("AOC_Day4.xlsx", header=None, names=["Tasks"])
df[["Team1_Tasks", "Team2_Tasks"]] = df["Tasks"].str.split(",", expand=True)
df[['T1_Start', 'T1_End']] = df["Team1_Tasks"].str.split("-", expand=True)
df[['T2_Start', 'T2_End']] = df["Team2_Tasks"].str.split("-", expand=True)
count = 0
for (index, row) in df.iterrows():
    # if (int(df['T1_Start'][index]) >= int(df['T2_Start'][index])) and (int(df['T1_End'][index]) <= int(df['T2_End'][index])):
    #     count += 1
    # elif (int(df['T2_Start'][index]) >= int(df['T1_Start'][index])) and (int(df['T2_End'][index]) <= int(df['T1_End'][index])):
    #     count += 1
    if (int(df['T1_Start'][index]) >= int(df['T2_Start'][index])) and (int(df['T1_Start'][index]) <= int(df['T2_End'][index])) \
            or \
            (int(df['T1_End'][index]) >= int(df['T2_Start'][index])) and (int(df['T1_End'][index]) <= int(df['T2_End'][index])):
        count += 1
    elif (int(df['T2_Start'][index]) >= int(df['T1_Start'][index])) and (int(df['T2_Start'][index]) <= int(df['T1_End'][index])) \
            or \
            (int(df['T2_End'][index]) >= int(df['T1_Start'][index])) and (int(df['T2_End'][index]) <= int(df['T1_End'][index])):
        count += 1


print(count)
print("Maulik")