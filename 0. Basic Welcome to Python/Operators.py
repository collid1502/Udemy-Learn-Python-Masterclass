"""
Numeric Operators in Python
"""

a = 12
b = 3

print(a + b)   # 15
print(a - b)   # 9
print(a * b)   # 36
print(a / b)   # 4.0
print(a // b)  # 4  integer division, rounded down towards minus infinity
print(a % b)   # 0 modulo:  the remainder after integer division

print()
for i in range(1, 4):
    print(i)    # This prints out 1,2,3 to the console

# we would need to do integer division ... because if we use a float for a Loop when i passes as whole numbers (integers)
# so
"""
print()
for i in range(1, a / b):  # this will error due to float result from single slash division code
    print(i)
"""

print()
for i in range(1, a // b):  # this will work
    print(i)

# coding exercise
# a shop sells buns for $2.40 each. How many buns can a customer get with $15 ?
# remember, you cant sell less than a whole bun!

bun_price = 2.40
money = 15
print(money / bun_price)   # This will give 6.25 (which is the correct answer, but we cant seel a quarter of a bun, so to round down
print(money // bun_price)  # The integer division method rounds downwards towards minus infinity, so turns the 6.25 into the integer 6

"""
--------------------------------------------------------------------------------------------------------------------------------------------------
"""

"""
Operator Precedence in Python 
"""
print(a + b / 3 - 4 * 12)   # the answer Python gives is: -35.0

# remember BODMAS - >  Brackets, Order (exponents), Division, Multiplication, Addition, Subtraction

print(a + (b/3) - (4 * 12))   # This also evaluates to -35.0

print((((a+b) /3) -4) * 12)   # And this would provide the answer 12.0


