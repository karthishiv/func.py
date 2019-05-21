#py1_factor_of_num_N
def  print_factor(n):
    for i in range(1,n+1):
        if (n%i==0):
            print(i)
n=320    
print(print_factor(n))

#py2_find_primeORnot
n=9
if(n>1):
    for i in range(2,n):
        if (n%i)==0:
            print(n," not prime")
            break
    else:
        print(n," prime")
else:
    print(n,"not prime")
    
    
 #py3_find_primeNOs_btwn_2intervals 
 l=15
up=99
print("prime nos. btwn", l ,"and", up ,"are:")
for n in range(l,up+1):
    if(n>1):
        for i in range(2,n):
            if (n%i)==0:
                break
        else:
            print(n)
    
#py4_find_prime_factors
def prime_factors(n):
    i=2
    factors = []
    while i*i <= n:
        if n%i:
            i+=1
        else:
            n//=i
            factors.append(i)
    if n>1:
        factors.append(n)
    return factors
n=320
print(prime_factors(n))

#py5_perfectORnot
n=10
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print(n," is a perfect number")
else:
    print(n," is not a perfect number")
    
 #py6_perfectSqrORnot
 
 import math
n=int(input())
i=int(math.sqrt(n))
if(n==i*i):
    print(n," is a perfect square number")
else:
    print(n," is not a perfect square number")
    
   #py7_perfectSqr_2intervals
   
 def CountSquares(a, b): 

	cnt = 0 

	 
	for i in range (a, b + 1): 
		j = 1; 
		while j * j <= i: 
			if j * j == i: 
				cnt = cnt + 1
			j = j + 1
		i = i + 1
	return cnt 
a = 9
b = 25
print ("Count of squares is:", CountSquares(a, b) )


#Py8_check_no_is_powerof2ORnot

n=int(input())
for i in range(1,n+1):
    if(n==2**i):
        print(n," is a power of two")
        break
else:
    print(n," is not a power of two")
