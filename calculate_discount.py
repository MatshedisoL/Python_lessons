# Question 1
def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price

original_price = 200.0
discount = 25.0

final_price = calculate_discount(original_price, discount)
print(f"The final price is: ${final_price:.2f}")
print(f"Original Price: ${original_price}")
print(f"Discount: {discount}%")

# Question 2

def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompting the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount)

    # Print the result
    if final_price == original_price:
        print(f"No discount applied. The price remains: ${original_price:.2f}")
    else:
        print(f"Discount applied! The final price is: ${final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")

