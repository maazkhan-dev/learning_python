#defining tuples
tuple1= ("apple", "banana", "cherry", "apple", "cherry")  #unchangible & allow duplication
print(tuple1)

print(type(tuple1))

# accessing list items
print(tuple1[1])
print(tuple1[-1])
print (tuple1[2:4])
print(tuple1[:2])
print(tuple1[3:]) 

#Convert the tuple into a list to be able to change it & than convert again into tuple
#As tuple is immutable & can't changes 
y = list(tuple1)
y[1] = "kiwi"
print (y)
print(type(y))
tuple2= tuple(y)
print(tuple2)

# Loop through a tuple
for fruit in tuple1:
  print(fruit)