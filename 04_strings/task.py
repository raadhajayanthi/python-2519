student_id = int(input("enter student id "))
student_name = str(input("enter student name "))
student_attendance = int(input("enter attendance "))
student_noofsubjects = int(input("enter no of subjects "))
student_totalscore = 0

for enterscores in range(student_noofsubjects):
     enterscores =  int(input("enter scores of subject " +str(enterscores)))
     student_totalscore = student_totalscore +  enterscores   

student_averagescore = student_totalscore/student_noofsubjects

if student_averagescore >= 85:
  student_performancelevel = "Excellent"
elif (student_averagescore >= 70) and (student_averagescore <= 84):
   student_performancelevel = "Good"
elif (student_averagescore >= 50) and (student_averagescore <= 69):
   student_performancelevel = "Average"
else:
   student_performancelevel = "Needs Improvement"  

if student_attendance < 0.75:
   student_attendance = "Low Attendance"
else:
   student_attendance = "OK Attendance Satisfied"  


print(f"student’s ID: ",student_id)
print(f"student name: ",student_name)
print(f"student totalscore: ",student_totalscore)
print(f"student averagescore: ",student_averagescore)
print(f"student performancelevel: ",student_performancelevel )
print(f"student attendance: ", student_attendance) 