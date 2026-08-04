n=[1,2,3,4,5,6,7,8,9,10]
freq={}
for num in n:
    freq[num]=freq.get(num,0)+1
print(freq)
