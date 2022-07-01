#Write your code below this row 👇
def add_evens(nums):
    total = 0
    range_num = range(nums+1)
    for num in range_num:
        if(num % 2 == 0):
            total += num
    print(total)

add_evens(100)