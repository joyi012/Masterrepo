def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks / total_subjects
    return average_marks

marks = [40, 20, 30, 32, 45, 60]
average_marks = find_average_marks(marks)
print("Your average marks is:", average_marks)
