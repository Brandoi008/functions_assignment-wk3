def calculate_discount(price, discount_percent):

  if discount_percent >= 20:
    discount = price * discount_percent / 100
    final_price = price - discount
  else:
    final_price = price

  return final_price

while True:
  try:
    original_price = float(input("Enter the original price of the item ($): "))
    discount_percent = float(input("Enter the discount percentage (0-100): "))
    if 0 <= discount_percent <= 100:
      break
    else:
      print("Invalid discount percentage. Please enter a value between 0 and 100.")
  except ValueError:
    print("Invalid input. Please enter numbers for price and discount percentage.")

final_price = calculate_discount(original_price, discount_percent)
print(f"Original price: ${original_price:.2f}")
print(f"Discount applied: {discount_percent:.2f}%")
print(f"Final price: ${final_price:.2f}")
