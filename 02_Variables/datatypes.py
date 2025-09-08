# Data Types 
num = 10 # int 
print(type(num))
      
num = 10.0 # float 
print(type(num))

num = 1 + 2j # complex
print(type(num))

data = "hello" # string
print(type(data))

data = "h" # string
print(type(data))

canVote = True
print(type(canVote))

list_nums = [10,20,30,10]
list_colors = ["blue","red","green"]
print(type(list_nums))
print(type(list_colors))
print(list_nums)

list_nums = (10,20,30,10)
print(type(list_nums))
print(list_nums)

list_nums = {10,20,30,10}
print(type(list_nums))
print(list_nums)

list_nums = {"n1":10,"n2":20,"n3":30}
print(type(list_nums))
print(list_nums)

x = None
print(type(x))
print(x)

class Student: # class
    pass # skip - do nothing 

edify_student = Student() # object
print(type(edify_student))