# break and continue keywords allow you to alter the flow of a loop.

# 1. break - immediately terminates the loop completely. The program resumes after the loop.
found = False
for i in range(100):
    if i == 42:
        found = True
        break

# 2. continue - skips the rest of the current iteration and jumps back to the start of the loop for the next item.
for i in range(10):
    if i % 2 ==0:
        continue
    print(i)