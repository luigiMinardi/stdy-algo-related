Current bubble sort implementation:
```py
def bubble_sort(nums):
    swap = True
    while swap:
        swap = False
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swap = True
    return nums
```
While it does sort, it does a lot of unnecessary computation since it's not taking into account that we already sorted the last numbers, so for example on this worst case scenario `[9, 8, 7, 6, 5, 4, 3, 2, 1]` its running `72` times the for loop, being very close to `n^2` and bubble sort should be close to n^2/2` instead.

To fix it you create a variable that save the length and reduce it on each while iteration:
```py
def bubble_sort(nums):
    swap = True
    loop_len = len(nums)
    while swap:
        swap = False
        for i in range(1, loop_len):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swap = True
        loop_len-=1
    return nums
```

And you could even use this variable instead the `swap` one on the `while` condition, making the code not only faster but easier to read:

```py
def bubble_sort(nums):
    loop_len = len(nums)
    while loop_len > 1:
        for i in range(1, loop_len):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
        loop_len-=1
    return nums
```

Pseudo Code of the last implementation of the algorithm:
```
Procedure bubble_sort(nums):
    Set LoopLength to nums length
    While LoopLength is greater than 1:
        For i from the 2nd element to the LoopLength:
            If the (i-1)th element of nums is greater than the ith element:
                Swap the (i-1)th element and the ith element of nums
        Set LoopLength to its value minus one
    Return nums
End Procedure
```
> For i from the 2nd element to the LoopLength:

You can also state this as:

`For i from the 2nd element to the element at the LoopLength -1 position:`
or something like:
`For i from the 2nd element to the element at the LoopLength (excluded) position:`

___________________ Matt response ___________________

Don't you think this is the fastest?
```py
def bubble_sort(nums):
    swap = True
    loop_len = len(nums)
    while swap:
        swap = False
        for i in range(1, loop_len):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swap = True
        loop_len-=1
    return nums
```

___________________
After a few experimentations with it I got this new improved solution
___________________ My reply ___________________

OOOh now I get what you were saying.
Yeah, without the swap you'll have `n * (n - 1) / 2` comparisons and `n-1` passes through the list so you act as if it wasn't sorted,
while on the one with swap you check `n` times if it was swapped and return the list already.

So yeah, the one with `swap` is definitely more optimized in the best case scenario. (So the Big Omega of it is Omega(n))

You can still optimise the number of passes on the worst case though,
right now since you don't check for the `end` you'll run the `while` loop `n` times instead of `n-1`.

```py
def bubble_sort(nums):
    swap = True
    end = len(nums)
    while swap and end > 1:
        swap = False
        for i in range(1, end):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swap = True
        end-=1
    return nums
```

And I think this is the best that we can optimize the Bubble Sort to have the worst case as `n-1` passes and `n * (n - 1) / 2` comparisons (so basically `n * (n + 1) / 2` total) and the best case as `1` passe and `n-1` comparisons so `n` total.


