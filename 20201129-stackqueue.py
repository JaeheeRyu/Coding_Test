nums = [4, 1, 2, 3, 1, 0, 5]

location = []
location.append(0)
for i in range(len(nums)):
    if i != 0:
        #print(nums[location[-1]])
        location.append(location[-1]+nums[location[-1]])