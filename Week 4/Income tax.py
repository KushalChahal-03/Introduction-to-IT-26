income = int(input("What is your income :"))
if income <= 20000 :
    tax = 0.02 * income
elif income <= 50000 :
    tax = 400 + 0.25 *(income - 20000)
else :
    tax = 1150 + 0.35 * (income - 50000)
print("Income tax :",tax)
