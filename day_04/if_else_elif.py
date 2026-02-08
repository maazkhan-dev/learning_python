age = 19
allowed_age = 18

#  Is he/She is allowed to access this site ?
#  if (age == allowed_age) :  #or simply   age==allowed_age:
#     print("You are allowed to access this site.")
# else:
#  print("You are not allowed to access this site.")

if (age == allowed_age) :  #or simply   age==allowed_age:
    print("You are allowed to access this site.")
elif (age > allowed_age) :                               
 print("You are 'STRONGLY' allowed to access this site.")
  # You can write multiple elif statement
elif ( age < 10) :
  print("You are a Kid! Can't access.")
else:
 print("You are not allowed to access this site.")

