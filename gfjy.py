from random import randint
nums = []
nums_count = 5
i = 0
while i < nums_count:
    rand_num = randint(0, 100)
    nums.append(rand_num)
    i = i + 1
for n in nums:
    print(n)
