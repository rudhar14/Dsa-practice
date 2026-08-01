n=int(input("enter your number : "))
original=n
result=0
while n>0:
    last_digit=n%10
    result=(result*10)+last_digit
    n=n//10
    
if (original==result):
    print("palindrome")
    
else:
    print("not palindrone")