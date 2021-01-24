# Given an array containing None values fill in the None values with most recent
# non None value in the array
array1 = [1,None,2,3,None,None,5,None]

def solution1(array):
    valid = 0
    res = []
    for i in array:
        if i:
            res.append(i)
            valid = i
        else:
            res.append(valid)
    return res

print(solution1(array1))

def solution2(array):
    last = 0
    for i in range(len(array)):
        if array[i] is None:
            array[i] = last
        else:
            last = array[i]
    return array
print(solution2(array1))

