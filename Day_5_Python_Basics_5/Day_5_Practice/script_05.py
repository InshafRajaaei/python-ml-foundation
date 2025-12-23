# Script 5: The Flexible Adder (*args)

# 1. Create a function super_sum that takes *args.
# 2. It should loop through all numbers passed to it and return the total.
# 3. Test it with 2 numbers, then 5 numbers, then 10 numbers

def super_sum(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total

print(super_sum(5,10))
print(super_sum(28,72,82,1,35))
print(super_sum(1,23,4,5,6,7,8,9,10))