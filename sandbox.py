nums = [2, 7, 11, 15] 
target = 17

def twoSum (nums, target): 
    for i in range(len(nums)):
        print("\nThe i indices: ", i, "The current num is:", nums[i])
        for j in range(i+1, len(nums)):
            print("The j indices: ", j, "The current num is:", nums[j])
            if nums[i] + nums[j] == target:
                return [i,j]

twoSum(nums, target)
result = twoSum(nums, target)
print("\n \n Result: ", result)