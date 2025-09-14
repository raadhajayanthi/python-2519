#Student Grade and fee Tracker
#identifiers - operators - variables - datatypes - strings


print("="*50)
print("       Student Grade and Fee Tracker")
print("="*50)


#Student Id
student_id_valid = False
while not student_id_valid:
    student_id = input("Enter Your ID ")

    #check for negative numbers (-10)
    if student_id.startswith("-") and student_id[1:].isdigit():
       print("Please Enter Positive Number as ID ")

    #CHECK FOR DIGITS ONLY AND ABOVE ZERO   
    elif student_id.isdigit():
         student_id = int(student_id)
         if student_id > 0:
          student_id_valid = True
         else:
           print("Please Enter Non Zero Value for ID ")

    else:
      print("Enter Numbers Only as ID ")   


student_id = str(student_id) 
print("EDIFY" ,student_id )

#student name
student_name_valid = False
while not student_name_valid:
  student_name = input("enter name ")

  student_name = student_name.strip().title()
  #print("student name ", student_name)

 #validate given name - no spaces in names also
  name_for_check = student_name.replace(" ","")

 #isalpha will work only with the above statement so thats y we wrote no spaces 
  if name_for_check.isalpha() and len(student_name) >= 3:
     student_name_valid = True 
     print("welcome " + student_name)

  else:
     if not name_for_check.isalpha():
      print("Enter Name only in Alphabets ")
     elif len(name_for_check) < 3:
      print("Enter Minimum of 3 characters ") 
     

subject_score = int(input("enter subject score(1-100) "))

first_name = student_name.strip().split()[0].lower()
print("first name" , first_name)

University_Email = f"{first_name}.{student_id}@edify.edu"
print(f"University Email {University_Email}")

# course fee validation & calculation
base_course_fee_valid = False
while not base_course_fee_valid:
    base_course_fee = input("Enter Course Fee: ")
    if base_course_fee.isdigit():
        base_course_fee = int(base_course_fee)
        if base_course_fee > 0:
            base_course_fee_valid = True
        else:
            print("Enter Positive Number For Fee")
    else:
        print("Course Fee can be only numbers")

discount = 0
coupon = input("Enter coupon code ")

# if "PROMO" in coupon -> operator 
if coupon.find("PROMO") != -1:
    discount = 5000

# if "PROMO" in coupon -> operator 
# if "PROMO" in coupon:
#     discount = 5000

final_fee = base_course_fee - discount
print(f"Actual Fee: {base_course_fee} ")
print(f"Discount Applied: {discount} ")
print(f"Fee To Pay: {final_fee}")

    