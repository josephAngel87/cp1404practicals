number_of_items = int(input("Enter number of items: "))
total_price = 0

for i in range(number_of_items):
    price = float(input("Enter price: "))
    total_price = price + total_price
print()

if total_price > 100:
    total_price = total_price * 0.9

print(f"Total price of {number_of_items} items is ${total_price:.2f}")
