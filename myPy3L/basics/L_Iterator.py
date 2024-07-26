# Iteration
nlist = [1, 3, 5, 7, 9]
for key in nlist:
    print(key - 1)

# List generation
l = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in l])

# a simple implementation of quicksort in Python
def quicksort(arr):  
    if len(arr) <= 1:  
        return arr  
    else:  
        pivot = arr[0]  
        left = [x for x in arr[1:] if x <= pivot]  
        print('left: Numbers less than or equal to ', pivot)
        print(left)
        right = [x for x in arr[1:] if x > pivot]  
        print('right: Numbers greater than ', pivot)
        print(right)
        return quicksort(left) + [pivot] + quicksort(right)

arr = [3, 0, 8, 5, 2, 4, 1, 6, 7, 9]  
sorted_arr = quicksort(arr)  
print(sorted_arr)
# 1, len(arr)=10,   return quicksort([0,2,1]) + [3] + quicksort([8,5,4,6,7,9])

# ---先递归 quicksort([0,2,1]) 
    # 2, len(arr)=3,    return {quicksort([]) + [0] + quicksort([2,1])}
    # ---此时 quicksort([])递归结束，结果为 []；
    # ---开始递归 quicksort([2,1])
        # 3, len(arr)=2,    return {quicksort([1]) + [2] + quicksort([])}
    # ---此时 quicksort([2,1])递归结束，结果为 [1,2]；
# ---此时 quicksort([0,2,1])递归结束，结果为 [0,1,2]；

# ---开始递归 quicksort([8,5,4,6,7,9])
    # 4, len(arr)=6,    return {quicksort([5,4,6,7]) + [8] + quicksort([9])}
    # ---开始递归 quicksort([5,4,6,7])
        # 5，len(arr)=4,    return {quicksort([4]) + [5] + quicksort([6,7])}
        # ---此时 quicksort([4])递归结束，结果为 [4]；
        # ---开始递归 quicksort([6,7])
        # 6，len(arr)=2,    return {quicksort([]) + [6] + quicksort([7])}
        # ---此时 quicksort([6,7])递归结束，结果为 [6,7]；
    # ---此时 quicksort([5,4,6,7])递归结束，结果为 [4,5,6,7]；
# ---此时 quicksort([8,5,4,6,7,9])递归结束，结果为 [4,5,6,7,8,9]；

# ---此时 全部结束，结果为 [0,1,2,3,4,5,6,7,8,9]；