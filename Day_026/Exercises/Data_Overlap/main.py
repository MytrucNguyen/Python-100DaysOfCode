from unittest import result


with open("file1.txt") as data1:
    list1 = data1.readlines()

with open("file2.txt") as data2:
    list2 = data2.readlines()

result = [int(num) for num in list1 if num in list2]

print(result)
