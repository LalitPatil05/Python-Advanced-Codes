import sys
randomList = ['a', 0, 2]

for i in randomList:
    try:
        print("The entry is  ", i)
        r = 1/int(i)
    
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
        
print("The reciprocal of", i, "is", r)
