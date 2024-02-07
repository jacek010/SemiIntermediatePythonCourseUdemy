import time
import functools


@functools.lru_cache()
def factorial(n):
    time.sleep(0.1)
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


for i in range(1, 11):
    print(f"{i}! = {factorial(i)}")

print(factorial.cache_info())
