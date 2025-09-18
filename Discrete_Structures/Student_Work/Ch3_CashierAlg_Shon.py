#Algorithm to deduce minimum change that can be used to provide the amount listed in the change_needed variable. This algorithm should
#be able to use bills and coins, including: $100 bills, $50 bills, $20 bills, $10 bills, $5 bills, $2 bills, $1 bills, quarters, dimes, nickels, 
#and pennies.

total_cost = float(input("Input the total cost of the items purchased (number only, no dollar signs): "))
payment_rendered = float(input("Input the total amount of payment rendered (number only, no dollar signs): "))
change_needed = payment_rendered - total_cost
change_needed = round(change_needed, 2)

hundred_bill = 100.00
fifty_bill = 50.00
twenty_bill = 20.00
ten_bill = 10.00
five_bill = 5.00
two_bill = 2.00
one_bill = 1.00
quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01
change_given = []
bills_and_coins = [hundred_bill, fifty_bill, twenty_bill, ten_bill, five_bill, two_bill, one_bill, quarter, dime, nickel, penny]


if payment_rendered < total_cost:
    print("Insufficient payment rendered. Please provide an amount equal to or greater than the total cost.")
else:
    for bill_or_coin in bills_and_coins:
      while change_needed >= bill_or_coin:
            change_given.append(bill_or_coin)
            change_needed -= bill_or_coin
            change_needed = round(change_needed, 2)
    print("The change given is: ", [f"${bill_or_coin_change:.2f}" for bill_or_coin_change in change_given])
    print(f"The total number of bills and coins given is: {len(change_given)}")
    print(f"The total amount of change given is: ${round(sum(change_given), 2)}" )
        






