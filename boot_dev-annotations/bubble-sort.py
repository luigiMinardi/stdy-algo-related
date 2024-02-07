def bubble_sort_mine(nums):
    swap = True
    while swap:
        swap = False
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swap = True
    return nums

# 9 72 36

def bubble_sort_improoved(nums):
    swap = True
    len_nums = len(nums)
    while swap:
        swap = False
        for i in range(1, len_nums):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swap = True
        len_nums-=1
    return nums

# 9 36 36
# 1 8 8 (already sorted list)

# best Theta option
def bubble_sort_theta(nums):
    swap = True
    len_nums = len(nums)
    while swap and len_nums > 1:
        swap = False
        for i in range(1, len_nums):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swap = True
        len_nums-=1
    return nums

# 8 36 36
# 1 8 8 (already sorted list)

def bubble_sort(nums):
    loop_len = len(nums)
    while loop_len > 1:
        for i in range(1, loop_len):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
        loop_len-=1
    return nums

# 8 36 36

# Me implementing prime's bubble sort in python
def bubble_sort_prime(nums):
    last = len(nums) -1
    i = 0
    while last > 0:
        if nums[i] > nums[i+1]:
            nums[i+1], nums[i] = nums[i], nums[i+1]
        i+=1
        if i == last:
            last -= 1
            i = 0
    return nums

# 8 36 36

'''
Comments like 9 36 36 are worst case scenario given the list:
[9,8,7,6,5,4,3,2,1]
Comments like 1 8 8 are best case scenario given the already sorted list:
[1,2,3,4,5,6,7,8,9]

The ones without best case either doesn't do best case properly (try to sort an already sorted list)
or I didn't tested the best case in it (should be 1 8 8 if done properly btw)
'''

