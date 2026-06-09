a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

print("Before swapping:")
print("a =", a)
print("b =", b)
print("c =", c)

a, b, c = b, c, a

print("After swapping:")
print("a =", a)
print("b =", b)
print("c =", c)
