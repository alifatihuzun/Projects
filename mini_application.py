upper_limit = 50000

store_name = input("Please enter your store name\n")
income = int(input("Please enter your income\n"))

if income > upper_limit:
    print("Congratulations!! "+store_name)
elif income < upper_limit:
    print("Alert!! Low Income "+str(income))
else:
    print("Go on!!")
