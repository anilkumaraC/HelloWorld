is_hot=False
is_cold=False

if is_hot:
    print("it'a hot day")
    print("drink plenty of water")
elif is_cold:
    print("its a cool day")
    print("Wear warm cloths")
else:
    print("it's a lovely day")
print("enjoy your day")





price=100000
has_good_credit=False
if has_good_credit:
    down_payment=0.1*price
else:
    down_payment=0.2*price
print(f"Down payment:  ${down_payment}")



has_high_income=True
has_good_credits=True
has_criminal_record=False
if has_good_credits and not has_criminal_record:
    print("he is eliglible for loan")


temperature=30
if temperature > 30:
    print("it's a hot day")
else:
    print("it's a not a hot day")



name="anil"
if len(name)<3:
    print("name must be at last 3 charecters")
elif len(name)>50:
    print("name must be a maximum of 50 charecters")
else:
    print("name looks good")


weight=int(input("weight:"))
unit=input('(L)bs or (K)g: ')
if unit.upper()=="L":
    converted=weight*0.45
    print(f"you are {converted} kilos")
else:
    converted=weight/0.45
    print(f"you are {converted} pounds")
