price = float(input("Enter the price: "))
discount = float(input("Enter a discount: "))

final_price = price - (price * discount / 100)
print("Discounted price:", final_price)
