def calculate_average(marks):
    return round(sum(marks) / len(marks), 2)

student_marks = [78, 84, 91, 87]

average_mark = calculate_average(student_marks)

print("Average:", average_mark)