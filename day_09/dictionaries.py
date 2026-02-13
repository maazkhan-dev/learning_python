#defining Dictionaries    #store data values in key:value pairs
#Changeble & Duplication Not Allowed (will overwrite the Previous one)
user_profile = {
    "username": "coder_bhai",          
    "followers": 2500,
    "is_active": True,
    "interests": ["Python", "Hiking", "gym"],
    "followers": 1000 #this will overwrite 2500
}         
print(user_profile)    

#Accessing items
x= user_profile["followers"]
print(x)

#By get() methods
y = user_profile.get('is_active')
print(y)

#key() Methods 
z = user_profile.keys()
print(z)

#Adding new pair
user_profile['age']= 23
print(user_profile) 
#Or through update() methods
user_profile.update({'hobby':'reading'})
print(user_profile)

#Removing item
user_profile.pop('age')  #popitem will remove the last inserted item #also .cleae() will empty the entire dictionary
print(user_profile)

#using del will remove the key with value
del user_profile["is_active"] 
print(user_profile)

#using for loop for printing keys
for x in user_profile: #Or for x in user_profile.keys()
 print(x)

 #for printing values
for x in user_profile: #Or for x in user_profile.values()
 print(x)
 print(user_profile[x])

