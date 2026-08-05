nums = [1, 2, 3, 4, 5, 6, 7, 8]

def func(nums, left, right):
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    func(nums, left + 1, right - 1)

def reverse_array(nums):
    func(nums, 2 , len(nums) - 1)
    return nums

print(reverse_array(nums))