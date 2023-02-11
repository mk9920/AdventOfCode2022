import pandas as pd
df = pd.read_fwf("input.txt", header=None)
# "Apply" a function along an axis of the DataFrame.
#Converting int datatype to string
df[0] = df[0].apply(str)
df1 = (df[0].str.split("", expand=True))
# iloc[initial row:ending row, initial column:ending column]
df1 = df1.iloc[:, 1:-1]
#apply map Apply a function to a Dataframe elementwise.
df1 = df1.applymap(int)

# Function to count boundary elements

shape = df1.shape
rows = shape[0]
columns = shape[1]
trees_on_bon = rows * 2 + (columns - 2) * 2

count = 0
visb_score= []
for row in range(1, rows-1):
    for column in range(1, columns-1):
        lft_cnt = 0
        rgt_cnt = 0
        top_cnt = 0
        bottom_cnt = 0
        tree = df1.iloc[row, column]
        left_trees = df1.iloc[row, :column]
        #Check if tree is visible form left side
        right_trees = df1.iloc[row, column+1:]
        top_trees = df1.iloc[:row, column]
        bottom_trees = df1.iloc[row+1:, column]
        if (tree > left_trees.max()) or (tree > right_trees.max()) or\
            (tree > top_trees.max()) or (tree > bottom_trees.max()):
            count += 1
        for item in left_trees.to_list()[::-1]:
            if tree > item:
                lft_cnt += 1
            elif tree <= item:
                lft_cnt += 1
                break
        for item in right_trees.to_list():
            if tree > item:
                rgt_cnt += 1
            elif tree <= item:
                rgt_cnt += 1
                break
        for item in top_trees.to_list()[::-1]:
            if tree > item:
                top_cnt += 1
            elif tree <= item:
                top_cnt += 1
                break
        for item in bottom_trees.to_list():
            if tree > item:
                bottom_cnt += 1
            elif tree <= item:
                bottom_cnt += 1
                break
        total_cnt = lft_cnt * rgt_cnt * top_cnt * bottom_cnt
        visb_score.append(total_cnt)

visible_trees = count + trees_on_bon
#Answer1
print(visible_trees)
#Answer 2
print(max(visb_score))