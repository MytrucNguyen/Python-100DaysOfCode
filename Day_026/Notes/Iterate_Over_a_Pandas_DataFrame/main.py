student_dict = {
    "student": ["Alex", "Bob", "Cat"],
    "score": [53, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
print("")

# Loop Through rows of data frame
for (index, row) in student_data_frame.iterrows():
    print(row)
    print("")
    print(row.student)
    print("")
    print(row.score)
    print("")
    if(row.student == "Alex"):
        print(row.score)
