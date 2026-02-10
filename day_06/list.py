#Defining list 
list = ["apple", "banana", "cherry", "mango", "strawberry"]
print(list)

# accessing list items
print(list[1])
print(list[-1])
print (list[2:4])
print(list[:2])
print(list[3:])

#changing list items
list[1] = "pineapple"
print(list)

#adding to List
list.append("orange")
print(list)

list.insert(1,"graps") #adding on specific index
print(list)

#Removing from list
list.remove("cherry") #pop() is for last 
print(list)

#loop through tye index n0.
for fruit in list :
    print(fruit)

#Joining list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)