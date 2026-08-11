nums=[55,43,97,-55,66,77,88,99]
largest=float("-inf")
second_largest=float("-inf")
n=len(nums)
for i in range(0,n):
    if nums[i]>largest:
        largest=nums[i]
for i in range(0,n):
    
    if nums[i]>second_largest and nums[i]!=largest:
        second_largest=nums[i]
                         
print(largest)
print(second_largest)