print("Program is Starting..!!")
print()



a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

try:
        c = a/b
        print("Divison is : ",c)

except ZeroDivisionError as e:
    print("Type of Exception :",e)


finally:
    print("It is a Final Block of Code")


print()
print("Program Ending")
