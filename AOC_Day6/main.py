import pandas as pd
df = pd.read_fwf("input.txt", header=None)
all_elemets = [alphabet for alphabet in df[0].tolist()[0]]
test_list = all_elemets
start = 0

##Sol 1:
# for item in range(len(all_elemets)-3):
#     first_item = all_elemets[item]
#     second_item = all_elemets[item+1]
#     third_item = all_elemets[item+2]
#     fourth_item = all_elemets[item+3]
#     sub_list = [first_item, second_item, third_item, fourth_item]
#     # set() method is used to convert any of the iterable to sequence of iterable elements with distinct elements
#     count_unique = len(set(sub_list))
#     if count_unique == 4:
#         print(sub_list)
#         print(item+4)
#     # It terminates the current loop and resumes execution at the next statement, just like the traditional break statement in C.
#         break

##Sol2:

for index in range(len(all_elemets)-14):
    sub_list = []
    for sub_index in range(index, index+14):
        sub_list.append(all_elemets[sub_index])
    count_unique = len(set(sub_list))
    if count_unique == 14:
        print(sub_list)
        print(index+14)
        break
print('M')

