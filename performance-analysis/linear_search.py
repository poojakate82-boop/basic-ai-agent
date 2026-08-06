import random
import time

# Create a list of 100000 random numbers
numbers = [random.randint(1, 1000000) for _ in range(100000)]

target = numbers[-1]

start = time.time()

for i in numbers:
    if i == target:
        break

end = time.time()

print("Target Found!")
print("Execution Time:", end - start, "seconds")