def fib():                              #fibonacci series function by def keyword
    print('fabonacci series:')          
    a=0
    b=1
    n=int(input('\nenter number of terms:'))
    print('\nterms:')
    print(' ',a,'\n ',b)
    while(n-2>0):                       #while loop
        c=a+b
        a=b 
        b=c
        print(' ',c)
        n-=1             

def mtab():                             #multiplication table function
    print('\nMultiplication table:')
    n=int(input('enter a number:'))
    for i in range(1,11):
        print('\n',n,' * ',i,' = ',n*i)

fib()                           #function called 
mtab()


n=int(input('\nenter a number:'))         #recursion for fibonacci
def rfib(x):    #here x is a variable input for a function
    if x==0 or x==1:           #conditional statements
        return 0
    elif x==2:
        return 1
    else:
        return rfib(x-1)+rfib(x-2)     #base case

for i in range(1,n+1):                      #returned value printed
    print('',rfib(i))


n=int(input('\nenter a number:'))              #factorial by recursion
def fact(x):                        
    if x==0 or x==1:
        return 1
    return x*fact(x-1)
print('factorial = ',fact(n))