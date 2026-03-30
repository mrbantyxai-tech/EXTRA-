marks = [78, 45, 89, 98, 67, 35, 56, 92, 88, 91,
         40, 73, 61, 29, 85, 77, 96, 54, 68, 21]

total_students = len(marks)
highest_marks = max(marks)
lowest_marks = min(marks)
average_marks = sum(marks) / total_students

passed = 0
failed = 0

for m in marks:
    if m >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

pass_percentage = (passed * 100) / total_students

sorted_marks = sorted(marks)

grade_A = 0
grade_B = 0
grade_C = 0
grade_D = 0
grade_E = 0
grade_F = 0

for m in marks:
    if m >= 90:
        grade_A = grade_A + 1
    elif m >= 80:
        grade_B = grade_B + 1
    elif m >= 70:
        grade_C = grade_C + 1
    elif m >= 60:
        grade_D = grade_D + 1
    elif m >= 40:
        grade_E = grade_E + 1
    else:
        grade_F = grade_F + 1

print("Total Students:", total_students)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Average Marks:", average_marks)
print("Passed:", passed)
print("Failed:", failed)
print("Pass Percentage:", pass_percentage, "%")
print("Sorted Marks:", sorted_marks)

print("Grade A:", grade_A, "Students")
print("Grade B:", grade_B, "Students")
print("Grade C:", grade_C, "Students")
print("Grade D:", grade_D, "Students")
print("Grade E:", grade_E, "Students")
print("Grade F:", grade_F, "Students")
