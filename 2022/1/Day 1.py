#Advent of Code 2022 day 1
import os

#import the input file
input_file = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
ifc = input_file.read()
ifc = ifc.replace('\n\n', '],[')
ifc = ifc.replace('\n', ',')
ifc = '[' + ifc + ']'
#convert the string to a dictionary
ifc = eval(ifc)

def convert_to_dict(mylist):
    mydict = {}
    elf_num = 1
    for item in mylist:
        mydict[elf_num] = item

        elf_num += 1
    return mydict

def sum_numbers_of_list(mylist):
    sum = 0
    for item in mylist:
        sum += int(item)
    return sum



elves = convert_to_dict(ifc)
sum_keys = {}
for x in elves:
    sum_keys[x] = sum_numbers_of_list(elves[x])

#sort sumkeys by value
sorted_sum_keys = sorted(sum_keys.items(), key=lambda x: x[1], reverse=True)

#Answer to part 1:
print("Answer to part 1:")
print(sorted_sum_keys[0][1])

print("\n")
#Answer to part 2:
print("Answer to part 2:")
print(sorted_sum_keys[0][1]+ sorted_sum_keys[1][1] + sorted_sum_keys[2][1])

None