age=int(input("enter your age:"))
if (age>=18 and age<=60):
    if(age>50):
        print("elder person")
    print("eligible")

elif(age>60):
    print("senior citizen")
    if(age>100):
        print("dont lie")

else:
    print("too young")