def insertion_sort_mine(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]            
            for j in range(i,0,-1):
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums

'''
36 [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

Inputs: [4, 3, 2, 1]
         |   j_index   arr[j]   arr[j-1]  arr
j = 3    v 
         1 3 2 [2, 3, 4, 1]
         2 3 1 [2, 1, 3, 4]
         1 2 1 [1, 2, 3, 4]
'''
# Lane's
def insertion_sort_lane(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j-=1
    return nums

'''
45 [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

Inputs: [4, 3, 2, 1]
         |   j_index   arr[j]   arr[j-1]  arr
j = 6    v 
         1 4 3 [3, 4, 2, 1]
         2 4 2 [3, 2, 4, 1]
         1 3 2 [2, 3, 4, 1]
         3 4 1 [2, 3, 1, 4]
         2 3 1 [2, 1, 3, 4]
         1 2 1 [1, 2, 3, 4]
'''

# My improve
def insertion_sort_also_mine(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            j = i
            while j > 0 and nums[j-1] > nums[j]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j-=1
    return nums

'''
36 [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

j  = 3
[2, 3, 4, 1]
[2, 1, 3, 4]
[1, 2, 3, 4]

'''

