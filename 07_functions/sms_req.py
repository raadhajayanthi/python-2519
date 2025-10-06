#Implement Student Management System using Functions

#system setup fixed using tuples
SYSTEM_INFO = ("Edify Student Management Portal", "V1" ,"2025" ,"Edify University ")
ADMIN_INFO = ("Email", "Phone", "Room 201")

#display system info at start using functions

def display_system_info():
    
  print("="*50)
  print(f"     Welcome To: ", SYSTEM_INFO[0])
  print(f"    Developed By Students at: ", SYSTEM_INFO[3])
  print("="*50)




#student info is dictionary
students = {} #empty update while entering details

#build menu system
def show_menu():
 
    print("Choose an option from (1-5): ")
    print("1 = Add Student")
    print("2 = Modify Student")
    print("3 = Delete Student")
    print("4 = List Student")
    print("5 = Student skill search ")
    print("6 = Exit Student")



def add_student(students):
        student_id = input("Enter Student ID ")
        if student_id in students:
            print("ID already exists")

        else:
           name = input("Enter Name: ").title()

           scores = []
           while True:
                score_input = input("Enter Scores or done: ")
                if score_input == "done":
                   break
                if score_input.isdigit():
                    score = int(score_input)
                    if 0<= score <=100:
                        scores.append(score)
                    else:
                        print("Enter score between (0-100) ") 
                else:
                    print("score should be  only digits ")           
                


           skills = set()  
           while True: 
              skill_input  = input("enter skills or done: ")   
              if  skill_input == "done":
                    break
              skills.add(skill_input.title())

        #save student details
           students[student_id] = {
            "name":name,
            "scores": scores,
            "skills": skills
         }
           print("students added ") 
           print(students)
        



def modify_student(students):
        print("Modify Student")  
        student_id = input("Enter Student ID To Update")
        if student_id in students:
          new_name = input("Enter New Nmae: ").title()
          students[student_id]["name"] = new_name
          print("name updated")
        else:
            print("Student Does Not Exist")

    
        print(students)



def delete_student(students):
        print("Delete Student")  
        student_id = input("Enter Student ID To Delete")
        if student_id in students:
            remove = students.pop(student_id)
            print (remove)
        else:
            print("ID Doesnot Exist")    
        
        print(students)


def listing_student(students):
        print("Listing Student") 
        if not students:
            print("ID doesnot Exist")
        else:
            print("student details")    
       
            for sid, data in students.items():
                name = data["name"]
                scores = data["scores"]
                avg = sum(scores)/len(scores)
                High_score = max(scores)
                all_skills = data["skills"]
                count_skills = len(all_skills)
                print("====DETAILS=====")
                print(f"ID:{sid}")
                print(f"Name:{name}")
                print(f"All scores:{scores}")
                print(f"Avg Score:{avg}")
                print(f"All skills:{all_skills}")
                print(f"skills count:{count_skills}")


def search_student_by_skill(students):
      student_skill = input("enter student skill: ").title()
      matched_student = list(filter(lambda s: student_skill in students[s]['skills'] , students))
      if matched_student:
                print(f"Students With Skills {student_skill} :")
                for sid in matched_student:
                 print(f"Id: {sid}, Name: {students[sid]["name"]}")
      else:
        print(f"no student found with skill {student_skill} ")                                                                                                   


def existing_system(students):
        print("Exiting System")   
        print("="*50)
        print(f"     ADMIN CONTACT DETAILS")
        print("="*50)
        print(f"ADMIN PHONE: {ADMIN_INFO[1]}")
        print(f"ADMIN EMAIL: {ADMIN_INFO[0]}")



display_system_info()


while True:
    show_menu()
    choice = input("Enter Your Choice(1-6): ")
    
    if choice == "1":
        add_student(students) 
    elif choice == "2":
         modify_student(students)
    elif choice =="3":
         delete_student(students)
    elif choice =="4":
         listing_student(students)
    elif choice =="5":
         search_student_by_skill(students)    
    elif choice =="6":
         existing_system(students)
         break
    else:
         print("enter optons only (1-5): ")      
                       

