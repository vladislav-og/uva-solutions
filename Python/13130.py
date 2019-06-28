def check(nums):

    for i in range(len(nums)):
        if i != 0:
            if int(nums[i - 1]) != int(nums[i]) - 1:
                return "N"
    return "Y"


n = int(input().strip())
for n in range(n):
    nums = input().strip().split(" ")
    print(check(nums))
