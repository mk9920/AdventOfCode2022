import pandas as pd
df = pd.read_csv('input.txt', header=None)
df[['Action', 'Value']] = df[0].str.split(" ", expand=True)
Cycle = []
Total_cycle_count = []
for index, row in df.iterrows():
    if df['Action'][index] == 'noop':
        Cycle.append(1)
    elif df['Action'][index] =='addx':
        Cycle.append(2)
    else:
        print("Unknown value")
df['Cycle_to_complete'] = Cycle
Total_cycle_count = [sum(Cycle[:index+1]) for index in range(len(Cycle))]
df['Total_cycle_count'] = Total_cycle_count
df['Value'] = df['Value'].fillna(0)
value = df['Value'].apply(int).to_list()
value[0] += 1
value_cyc_end = [sum(value[:index+1]) for index in range(len(value))]
df['Value_cyc_end'] = value_cyc_end
# Find the signal strength during the
# 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?
#20*17 +60*17 +100*23 +140*22 + 180*21 +220*16=14040
print("M")
