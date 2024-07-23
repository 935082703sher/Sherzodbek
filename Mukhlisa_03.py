ages=[]
cost=0
total=0.00
while True:
    age = input("Enter the age of the guest: ")
    if age=="":
        break
    else:
        age_int=int(age)
        if age_int<=2:
            cost= cost+0.00
        elif age_int<=12:
            cost=cost+14.00
        elif age_int>=65:
            cost=cost+18.00
        else:
            cost=cost+23.00
        total+=cost
print("Total ticket price for all guests", total)

