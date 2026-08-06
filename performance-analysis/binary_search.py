import random
import time

# Create a sorted list of 100000 random numbers
numbers = sorted([random.randint(1, 1000000) for _ in range(100000)])

# Target element
target = numbers[-1]

# Start the timer
start = time.time()

# Binary Search
left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

# Stop the timer
end = time.time()

print("Target Found!")
print("Execution Time:", end - start, "seconds")