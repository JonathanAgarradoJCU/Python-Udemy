def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor


divide(15, 2)

grades = [97, 85, 87, 66, 88]

average = divide(sum(grades), len(grades))

print(f"Your average grade is {average}.")
# print(divide(15, 2))
