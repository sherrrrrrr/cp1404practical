total_price = 0

while True:
    num_items = int(input("Number of items: "))
    if num_items <= 0:
        print("Invalid number of items!")
        continue

    for i in range(num_items):
        price = float(input("Price of item: $"))
        total_price += price

    if total_price > 100:
        total_price *= 0.9

    print(f"Total price for {num_items} items is ${total_price:.2f}")
    break
