#while Loops

# x=0
# while x<5:
#     print(x)
#     x=x+1

# For Loop

# for i in range(0,5):
#     print(i)

# use of for loop in array and break & continue
week_days = ['mon','tues','wed','thurs','fri','sat','sun']
# for days in week_days:
#     print(days)

for days in week_days:
    #if(days == 'thurs'): break
    if(days=='thurs'): continue
    print(days)
