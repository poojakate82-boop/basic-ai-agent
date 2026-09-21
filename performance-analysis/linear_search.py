import time

numbers = list(range(1, 100001))

#target = 100000   # Worst Case
target = 50000  # Average Case
# target = 1      # Best Case

start = time.time()

for i in numbers:
    if i == target:
        break

end = time.time()

print("Target Found!")
print("Execution Time:", end - start, "seconds")