# Given an array of integers, determine whether the array is monotonic or not.
A = [6, 5, 4, 4]
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]

def solution1(nums):
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1)))

def solution2(nums):
    return nums == sorted(nums) or nums == sorted(nums, reverse=True)

print(solution1(A))
print(solution1(B))
print(solution1(C))
print("###########")
print(solution2(A))
print(solution2(B))
print(solution2(C))
