nums = [-2, 3, -1, 4, -5, 2]
t = 0
maks = nums[0]

for i in range(len(nums)):

    t = t + nums[i]

    if t > maks:
        maks = t

    if t < 0:
        t = 0

print(maks)

