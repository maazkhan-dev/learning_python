# Defining sets 
set1 = {"apple", "banana", "cherry"}  #unordered, unchangeable*, and unindexed.
print(set1)
print(type(set1))


# Loop through the set, and print the values:
for fruit in set1:
  print(fruit)

#Adding items into sets
set1.add("mango")
print(set1)


# To add items from another set into the current set, useing  the update() method.  
tropical = {"pineapple", "kiwi"}
set1.update(tropical)
print(set1)

#remove an item in a set, using the remove(), or the discard() method.
set1.remove("kiwi")
set1.discard("pineapple")
print(set1)

#The clear() method empties the set:
tropical.clear()
print(tropical) 

#The del keyword will delete the set completely
del tropical

#joining two sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"Maaz", "khan"}
# set3 = set1.union(set2,set3)
#Or
set3 = set1 | set2 | set3
print(set3)