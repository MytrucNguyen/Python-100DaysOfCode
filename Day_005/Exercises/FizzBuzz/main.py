#Write your code below this row 👇

def FizzBuzz(last_num):
    nums = range(1, last_num+1)

    for num in nums:
        if(num % 15 == 0):
            print('FizzBuzz')
        elif(num % 3 == 0):
            print('Fizz')
        elif(num % 5 == 0):
            print('Buzz')
        else:
            print(num)

FizzBuzz(100)