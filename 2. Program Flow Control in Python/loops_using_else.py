numbers = [1, 45, 32, 12, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break

# When a loop finds a value not acceptable, code breaks out of the loop.
# That means the loop will only terminate normally if all the values are acceptable
# What we want to do, is run some code when the loop terminates normally.
# We don't want that code to execute if we break out of the loop, only when it
# goes all the way round.

numbers = [1, 45, 31, 12, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break

# No numbers are divisible by 8, so we don't break out of the loop, and thus, we reach the else after the loop
# has processed
else:
    print("All those numbers are fine")




