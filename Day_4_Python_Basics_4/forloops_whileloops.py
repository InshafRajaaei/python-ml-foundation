# 1. The for loop
# range(stop) - 0 to stop-1
# range(start, stop) - start to stop-1
# range(start, stop, step) - increments by step

# Sum of even numbers from 0 to 10
total = 0
for i in range(0, 11, 2):
    total +=i
print(total)

# 2. The while loop
# A while loop runs as long as conditions remain True. It is used when you don't know how many times the loop needs to run(waiting for user input. game loops).
count = 0
while count < 5:
    print(f"Count is {count}")
    count +=1
# The infinite Loop Trap: if the condition never becomes false, the program runs forever (until your computer freezes)
