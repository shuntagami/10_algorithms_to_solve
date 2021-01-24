#Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of 
#the non-zero elements.

array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]

def solution1(nums):
    for i in nums:
        if 0 in nums:
            nums.remove(0)
            nums.append(0)
    return nums

def solution2(nums):
    new_nums = [num for num in nums if num != 0]
    for i in range(nums.count(0)):
        new_nums.append(0)
    return new_nums

def solution3(nums):
    zeros = []
    non_zeros = []
    for n in nums:
        if n == 0:
            zeros.append(n)
        else:
            non_zeros.append(n)
    return non_zeros + zeros

print(solution1(array1))
print(solution1(array2))
print("########################################")
print(solution2(array1))
print(solution2(array2))
print("########################################")
print(solution3(array1))
print(solution3(array2))
