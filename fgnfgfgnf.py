from random import randint
nums = []
nums_count = 10
i = 0
while i < nums_count:
    rand_num = randint(0, 100)
    nums.append(rand_num)
    i = i + 1
new_nums = []
for n in nums:
    if n > 50:
        new_nums.append(n)
print(nums)
print(new_nums)
