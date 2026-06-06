from decimal import Decimal

x = str(1000000000**2 + 1)
print(Decimal(x) ** Decimal("0.5"))
# Decimal('1.41421356237309504880168872421')
