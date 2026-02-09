# print("hey! I'm learning python")
# print("hey! I'm learning python")
# print("hey! I'm learning python")


# # defining Function (way#01)
def hey() :
    print("hey! I'm learning python")
    print("hey! I'm learning python")
    print("hey! I'm learning python")

# # calling function (way#01)
hey()

#  (Way#02)
def hello():
    var = "I'm learning python"
    print(var)
    print(var)
    print(var)
hello()

#(Ways #03)
def passing_value (var):
     print(var)
     print(var)
     print(var)
passing_value('hey! I am passing values to Function')


# defining a function using if-elif-else
def school_calculator(age):
    if age == 5 :
        print("You are eligible for school")
    elif age > 5 :
        print('You should go to higher school')
    else :
        print('You are not eligible for school')
school_calculator(3)

#defining a function for future
def future_age(age) :
    new_age = age+10
    return new_age
    
current_age = future_age(21)  # calling the function and passing the value of age as 21
print(current_age)  # printing the returned value of the function which is the future age 
