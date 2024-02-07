# mine
def merge_sort_mine(nums):
    if len(nums) <2:
        return nums
    left = merge_sort_mine(nums[:(len(nums)//2)])
    right = merge_sort_mine(nums[(len(nums)//2):])
    return merge_mine(left, right)

def merge_mine(first, second):
    final = []
    i,j=0,0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i+=1
        else:
            final.append(second[j])
            j+=1
    if len(first) >i:
        final.extend(first[i:])
    if len(second) > j:
        final.extend(second[j:])
    return final


## Lane's:

def merge_sort_lane(nums):
    if len(nums) < 2:
        return nums
    first = merge_sort_lane(nums[: len(nums) // 2])
    second = merge_sort_lane(nums[len(nums) // 2 :])
    return merge_lane(first, second)


def merge_lane(first, second):
    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    return final



# Recursion monster

def merge_sort(nums):
    if len(nums) <2:
        return nums
    left = merge_sort(nums[:(len(nums)//2)])
    right = merge_sort(nums[(len(nums)//2):])

    final = []
    i,j=0,0
    return merge(left, right, final, i, j)

def merge(first, second, final, i, j):
    if i < len(first) and j < len(second):
        if first[i] <= second[j]:
            return merge(first, second,final + [first[i]],i+1, j)
        else:
            return merge(first, second,final + [second[j]],i, j+1)
    if len(first) > i:
        return merge(first,second,final + [first[i]],i+1,j)
    if len(second) > j:
        return merge(first,second,final + [second[j]],i,j+1)
    return final

