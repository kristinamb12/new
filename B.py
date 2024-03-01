n = int(input("n = "))
k = int(input("k = "))
from random import randint
nums = []
nums_count = n
i = 0
while i < nums_count:
    rand_num = randint(0, k)
    nums.append(rand_num)
    i = i + 1
for n in nums:
    print(n)