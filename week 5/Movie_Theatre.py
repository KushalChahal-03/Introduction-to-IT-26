movies = {"Dune": 12.5,"Barbie": 11.0,"Oppenheimer": 13.0,"Spirited Away": 10.0}
purchases = []  # list of (title, qty, price_each)
subtotal = 0
title = input("\n Enter movie title(or done): ").title()
while (title.lower() != "done"):
    if title not in movies:
        print("Available movies:\n " , "," .join(movies.keys()))
        title = input("\n Enter movie title(or done): ").title()
    qty = int(input("Enter quantity :"))
    if qty < 0:
        print("Please enter a positive number")
        continue
    purchases.append((title, qty, movies[title]))
    #subtotal += movies[title] * qty
    print("Current purchases:", purchases)
    title = input("\n Enter movie title(or done): ").title()

print("RECIEPT: \n")
for title, qty, price_each in purchases:
    line_total = qty * price_each
    subtotal += line_total
    print(title, " x", qty, " @ $",price_each," -> $", line_total)
	

print('Subtotal : $',subtotal)
tickets_by_movie ={}
revenue_by_movie ={}
for title, qty, price_each in purchases:
    tickets_by_movie[title] = qty
    revenue_by_movie[title]=(qty*price_each)
    print(tickets_by_movie)
    print("price", revenue_by_movie)
