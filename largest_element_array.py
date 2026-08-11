nums=[55,44,33,66,-77,66,97]
# 
largest=float("-inf")
n=len(nums)
for i in range(0,n):
    if nums[i]>largest:
        largest=nums[i]
print(largest)