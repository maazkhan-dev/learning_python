import module 
module.greeting('Mehran') 

#will take from the module.py file
x = module.person1['age']
print(x)

#the word Module can also be used as nickname
import module as md
md.greeting('Adeel haider')

x = md.person1['country']
print(x)

#There are several Built-in Module as well, Like
import platform

x = platform.system()
print(x)

#We can also import specific Methods/dictionary from module
from module import person1
print(person1['department'])