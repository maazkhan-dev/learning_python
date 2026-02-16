# None is a special constant in Python that represents the absence of a value.
#Assigning and Displaying a Non Value
x = None
print(x)

print(type(x))

# #Comparing to None (EXAMPLE)
# using is & is not identity operator

result = None 
if result is None:
    print('No result yet!')
else:
    print('result is ready!')

#OR
if result is not None:
    print('Result is Ready!')
else:
    print('No result Yet!')


#A method without a return Statement Returns None
def func():
  x = 3

x = func()
print(x) # It will return None 