"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero! Please enter a non-zero denominator.")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
    # 1. A ValueError occurs when a function receives an argument with an appropriate type but an unacceptable value.


except ZeroDivisionError:
    print("Cannot divide b  y zero!")
    #2. When the denominator is 0, a  ZeroDivisionError will occur.
print("Finished.")