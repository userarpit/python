
__all__ = ['prices']
from collections import Counter

prices = {"course": 97.99, "book": 54.99, "wallpaper": 4.99}
cart = Counter(course=1, book=3, wallpaper=2)

total = 0
for product, count in cart.items():
    subtotal = prices[product] * count 
    print(f"{product:9}: ${prices[product]:7.2f} × {count} = ${subtotal:7.2f}")
    total += subtotal

print(f"total amount is {total}")