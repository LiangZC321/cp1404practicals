total_price = 0
num = int(input("Number of items:"))
for i in range(0,num):
    price = float(input("price of item:"))
    total_price += price
    if total_price > 100:
        total_price = total_price * 0.9
print(f"Total price for {num} items is ${total_price} ")
