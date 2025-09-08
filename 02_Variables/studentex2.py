#student management system
student_id = 1
student_name = "raadha"
student_age = 29

quiz_score = 80
assignment_scodre = 75
exam_score = 90

student_attendance = 90

total_score = quiz_score + assignment_scodre + exam_score
avg_score = total_score/3

student_passed = avg_score > 70

student_attendance += 1

award_eligibility = student_attendance >= 90 and student_passed


print("=======student details========")
print(f"student name: {student_name}")
print(f"total score: {total_score}")
print(f"Student Average Score: {avg_score}")
print(f"Student Current Attendance: {student_attendance}")
print(f"Student Passed: {student_passed}")
print(f"Student Awarded: {award_eligibility}")

# Type Conversion -> Automatic / Implicit
a = 10
b = 3.5
c = a + b # 13.5
print(c)
print(type(c))

# Type Casting -> Manual / Explicit
x = 100
y = x
print(y)
print(type(y)) 
# explicit conversion
y = float(x)
print(y)
print(type(y))

# Data loss can occur
r = 3.14
value = int(r)
print(value)

# strings
value = "100"
print(type(value))
value_int = int(value)
print(value_int/10)
# print(value/10) # TypeError: unsupported operand type(s) for /: 'str' and 'int'

value = "hundred"
# value_int = int(value) # ValueError: invalid literal for int() with base 10: 'hundred'