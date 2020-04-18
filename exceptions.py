def divBy(number):
    try:
        return 42/number
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")

print(divBy(2))
print(divBy(0))
print(divBy(10))