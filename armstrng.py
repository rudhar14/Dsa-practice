n=int(input("enter your number: "))
original=n
total=0
no_digit=len(str(n))
while n>0:
    last_digit=n%10
    total=total+(last_digit**no_digit)
    n=n//10
if(original==total):
    print("armstrong")
else:
    print("not armstrong")