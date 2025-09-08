Student_name = input("enter student name")
Student_gradelevel = int(input(" enter student grade"))
Student_Basetuitionfee = int(input("enter base fee"))
Student_academic_topper = str(input("enter academic topper"))

  
#Student_BaseDiscount
if (Student_gradelevel >= 9) and (Student_gradelevel <= 12):

   if Student_academic_topper == "yes":
      Student_BaseDiscount = 0.20
   else:
      Student_BaseDiscount = 0.10   

elif (Student_gradelevel >= 6) and (Student_gradelevel <= 8):
       Student_BaseDiscount = 0.05

else:
       Student_BaseDiscount = 0


#Additional Discounts
if Student_gradelevel == 10:
    Student_Discount = Student_BaseDiscount + 0.03

elif Student_gradelevel == 12:
    Student_Discount = Student_BaseDiscount + 0.05

else:
    Student_Discount = Student_BaseDiscount + 0

    Student_Discount = Student_Discount * 100
    Student_final_discountamount = Student_Basetuitionfee * Student_Discount

    Student_Finaltuitionfee =  Student_final_discountamount - Student_Basetuitionfee 

    print("===========student details============:")
    print(f"student name:{Student_name}")
    print(f"Student gradelevel:{Student_gradelevel}")
    print(f"academic topper:{Student_academic_topper}")
    print(f"Student Basetuitionfee:{Student_Basetuitionfee}")
    print(f"student Total discount percentage :{Student_Discount}")
    print(f"student Final tuition fee after discount:{Student_Finaltuitionfee}")