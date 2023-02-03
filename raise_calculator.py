incomes = [1000,2000,3000,4000,5000]

def upper_raise(x):
    print(x + (x/5))

def lower_raise(x):
    print(x + (x/10))

for i in incomes:
    if i < 3000:
        upper_raise(i)
    elif i >= 3000:
        lower_raise(i)