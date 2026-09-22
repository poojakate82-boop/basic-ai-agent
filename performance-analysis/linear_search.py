import time

numbers = list(range(1, 50000000))
target = 50000000

start = time.time()

for num in numbers:
    if num == target:
        print("Target Found!")
        break

end = time.time()

print("Execution Time:", end - start, "seconds")

time.sleep(10)