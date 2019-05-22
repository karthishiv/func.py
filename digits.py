#py.sum_of_digits
num=int(input())
sum=0
while(num!=0):
    n=num%10
    sum=sum+n
    num=num//10
print(sum) 
#py.reverse_of_digits                #py.reverse_of_digits2
num=int(input())                      num=input()
reverse=0                             n=num[::-1]
while(num!=0):                        print(n)
    n=num%10
    reverse=(reverse*10)+n
    num=num//10
print(reverse)    

#py.reverse_of_string
num=input()
n=num[::-1]
if(num==n):
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")
   
#py.armstrong_number
num=int(input())
sum=0
temp=num
while(temp!=0):
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if(num==sum):
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstriong number")
    
 #py.gcd_numbers
import math
a=int(input())
b=int(input())
s=math.gcd(a,b)
print(s)

#py.lcm_numbers
import math
a=int(input())
b=int(input())
s=math.gcd(a,b)
lcm=a*b//s
print(lcm)    
