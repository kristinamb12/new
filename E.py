from random import randint
nums = []
nums_count = 10
i = 0
while i < nums_count:
    rand_num = randint(-100, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    nums.append(rand_num)
    i = i + 1
summ = 0
for n in nums:
    if n > 0:
        summ = summ + n
print(nums)
print(summ)