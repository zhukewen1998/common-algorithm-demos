nums = [23,2,4,6,2,5,1,6,13,54,8]

# ------------------快速排序A, 时间复杂度O(nlogn), 最坏的情况下O(n^2)-----------------------
# ------------------空间复杂度O(logn)-----------------------------------------------------
# ------------------不稳定排序------------------------------------------------------------
def quicksort(nums, left, right):
    if left >= right:
        return
    i, j = left, right
    while i < j:
        while nums[left] <= nums[j] and i < j:
            j -= 1
        while nums[left] >= nums[i] and i < j:
            i += 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[left], nums[i] = nums[i], nums[left]
    quicksort(nums, left, i-1)
    quicksort(nums, i+1, right)

# ------------------快速排序B, 时间复杂度O(nlogn), 最坏的情况下O(n^2)-----------------------
def quicksort2(nums, left, right):          # 用栈代替递归
    if left >= right:
        return
    stack = []
    while stack or left < right:
        if left < right:
            i, j = left, right
            while i < j:
                while nums[left] <= nums[j] and i < j:
                    j -= 1
                while nums[left] >= nums[i] and i < j:
                    i += 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            nums[left], nums[i] = nums[i], nums[left]
            stack.append((left, i, right))
            right = i - 1
        else:
            left, mid, right = stack.pop()
            left = mid + 1

quicksort2(nums, 0, len(nums)-1)
print(nums) 

# ------------------------快速排序的优化----------------------------
# ------------------------A三路快速排序-----------------------------
