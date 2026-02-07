#Logical Operators are true/false or 0/1
# equal to    ==
# not equal to  !=
# greater than  >
#less than    <
# greater than or equal to  >=
# less than or equal to  <=

#Is 5 is equal to 5
# print(5 == 5) #True

#Application of Logical Operator
# student_age = 19
# allowed_age = 18
# print(student_age>=allowed_age)
# print('You are allowed to access this site!')

#use of logical operator and input func

allowed_age = 18
age = input('how old is:')
#convert input into int 
print (type(age))
age = int(age)

print(age >= allowed_age) #this will throw an error because python take input in string '5' != 5
