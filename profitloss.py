actual_cost = float(input("Please enter the actual product price: "))
sale_amount = float(input("Please enter the sale price: "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print(f"Profit: Rs.{amount}")

else:
    amount = actual_cost - sale_amount
    print(f"Loss: Rs.{amount}")