#Week 4 tutorial
#Step 1 - Welcome
print("Welcome to Python coffee shop!")

#Step 2 - Ask for name
customer_name = input("\n What is your name ?")
print("Hi"+ customer_name +"Lets order some coffee!")

# Step 3 - Show Prices
p_coffee = 3.50
p_latte = 4.00
p_mocha = 5.00
print("\n Coffee : $"+ str(p_coffee))
print("Latte : $"+ str(p_latte))
print("Mocha : $"+ str(p_mocha))

# Step 4 - Print menu
menu = ("Coffee","Latte","Mocha","Espresso")
print("\n Our menu :",menu)

# Step 5 - Introduce while loop
flag = "yes"
total = 0
while flag == "yes" :
# Step 6 - Ask what the customer will order
    choice = input("\n What would you like to order(coffee/latte/mocha): ").lower()
    if choice == "coffee":
         cost = p_coffee
    elif choice == "latte":
         cost = p_latte
    elif choice == "mocha":
        cost = p_mocha
    else:
         print("Sorry, we do not have that.")
         cost = 0

# Step 7 - How many orders will it be
    quantity = int(input("\n How many cups would you like :"))

# Calculate the total amout for the order
    total_cost = cost * quantity
    total += total_cost
    flag = input("will you be ordering something else ? (yes/no):").lower()

# Ask if the customer is a  student, as a student gets 10% discount
student = input("\n Are you a student (yes/no): ").lower()
if student == "yes":
    print("You get a 10% discount !")
    total *=0.9
else :
    print("Sorry, you dont get a student discount")

# If ordered more that 1 item, customer gets a $1 discount
if quantity > 1:
    print("\n You get a discount of $1 !")
    total -= 1  # -= means you subtract 1 from the total_cost

# Print the final cost and thank you message
print("\n Your total is :$" + str(total))
print("\n Thank you, "+customer_name +"! Please come again!" )



