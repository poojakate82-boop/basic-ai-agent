import time

numbers = list(range(1, 100001))

#target = 50000    # Worst Case
#target = 75000  # Average Case
target = 100000 # Best Case

start = time.time()

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

end = time.time()

print("Target Found!")
print("Execution Time:", end - start, "seconds")
