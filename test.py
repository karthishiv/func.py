#return sum of elements of list
def sum(l,n):
    a=len(l)
    s=0
    for i in range(1,a-1):
        if(l[i-1]!=n and l[i+1]!=n and l[i]!=n):
            s+=l[i]
    if(l[1]!=n and l[0]!=n):
        s+=l[0]
    if(l[a-2]!=n and l[a-1]!=n):
        s+=l[a-1]
    return s
      
num_list=list(map(int,input().split()))
number=int(input())
print(sum(num_list, number))

#find num 9 btw 4index
def find(num):
    for i in range(0,len(num)):
        if(num[i]==9 and i<4):
            return True
    return False
        
  #edit your code here
num=list(map(int,input().split()))
print(find(num))

#num and digit counts
def countdigits(s):
    c1=0
    c2=0
    l=[]
    for i in s:
        if i.isalpha():
            c1+=1
        elif i.isnumeric():
            c2+=1
    l.append(c1)
    l.append(c2)
    return l
                
s=input()
print(countdigits(s))

#find 123 in list
def check(l):
    num=""
    for i in l:
        num=num+str(i)
    if "123" in num:
        return True
    else:
        return False
  

l=list(map(int,input().split()))
print(check(l))

#reversing from half
def exchange(l):
    a=[]
    b=[]
    c=len(l)//2
    for i in range(c):
        a.append(l[i])
    for i in range(c,len(l)): 
        b.append(l[i])
        b.sort(reverse=True)
    lis1t=b+a
    return lis1t
            
  
l=list(map(int,input().split()))
print(*(exchange(l)))

#adding ing and ly
def name(alphabet):
    if(len(alphabet)>=3):
        if (alphabet.endswith("ing")):
            alphabet=alphabet+"ly"
        else:
            alphabet=alphabet+"ing"
    return alphabet
alphabet=input()
print(name(alphabet))
 
#replace with preceding value
def replace(li):
    l=[]
    l.append(0)
    for i in range (0,len(li)-1):
        l.append(li[i]*2)
    return l
s=list(map(int,input().split()))
print(*(replace(s)))

#build_index_grid(rows,columns)
r,c=map(int,input().split())
l=[]
for i in range(0,r):
    n=[]
    for j in range(0,c):
        temp=str(i)+','+str(j)
        n.append(temp)
    l.append(n)
print("[",end="")
print(*l,sep=',\n',end="")
print("]")

#new dictionary
import ast
def new_dictionary(prices):
    n=ast.literal_eval(prices)
    new_dict={}
    for key,value in n.items():
        if value>200.0:
            new_dict[key]=value
    sorted_d=sorted(new_dict.items())
    return dict(sorted_d)
prices =input()
print(new_dictionary(prices))

#balanced brackets
def isValidPair(left,right):
    if left=='(' and right==')':
        return True
    if left=='{' and right=='}':
        return True
    if left=='[' and right==']':
        return True
    return False
def isProperlyNested(S):
    stack=[]
    
    for symbol in S:
        if symbol=='[' or symbol=='{' or symbol=='(':
            stack.append(symbol)
        else:
            if len(stack)==0:
                return False
            last =stack.pop()
            if not isValidPair(last,symbol):
                return False
    if len(stack)!=0:
        return False
    return True
N=int(input())
for _ in range(N):
    s=input()
    if isProperlyNested(s):
        print("YES")
    else:
        print("NO")
