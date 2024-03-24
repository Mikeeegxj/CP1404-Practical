import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3


# 1. I see the integer number in the line 1.
# The smallest number could I have seen was 5, the largest was 19.

# 2. I see the integer number in the line 2.
# The smallest number could I have seen was 3, the largest was 9.
# line 2 could not produce a 4

# 3. I see the integer number with the decimal.
# The smallest number could I have seen was 2.50000001, the largest was 5.49999999.

# 4.
print(random.randint(1, 100))  # line 4


