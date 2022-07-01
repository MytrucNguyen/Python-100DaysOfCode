# 🚨 Don't change the code below 👇
from numpy import equal, maximum, minimum


student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# Important you are not allowed to use the max or min functions. 
# The output words must match the example. i.e

def quick_sort(arr):
    elements = len(arr)
    
    if elements < 2:
        return arr
    
    current_position = 0 

    for i in range(1, elements): 
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp 
    
    left = quick_sort(arr[0:current_position]) 
    right = quick_sort(arr[current_position+1:elements]) 

    arr = left + [arr[current_position]] + right 
    
    return arr
    

def highest_score(arr):
    sorted_arr = quick_sort(arr)
    highest_score = sorted_arr[len(sorted_arr) -1]

    print(f"The highest score in the class is: {highest_score}")

highest_score(student_scores)