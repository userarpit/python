from decimal import Decimal, getcontext

getcontext().prec = 2
print(Decimal(0.112) + Decimal(0.234))  # Decimal('0.33')