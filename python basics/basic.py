'''Basic programs syntax'''

print('this is print statement')         #output line
n1=int(input('enter 1st number:'))       #input line
n2=int(input('enter 2nd number:'))
print(f'{n1,n2}')                       # similar as printf -> print(f'{var,value}')

str='string'                        #datatypes
fvar=4.54                               
bvar=True
nvar=None
print(type(n1),type(str),type(fvar),type(bvar),type(nvar))

print('arithematic operators:')           #arithematic operators        
print('add =',n1+n2,
      '\nsub =',n1-n2,
      '\nmul= ',n1*n2,
      '\ndivide = ',n1/n2,
      '\ninteger div =',n1//n2,
      '\nremainder =',n1%n2,
      '\nexpo =',n1**n2)

n=int(input('enter a number:'))

print('\nassignment operators:')         #assignment operator
n+=2
n-=2
n*=2
n/=2
n%=2
n//=2
n**=2
print('',n)

print('\ncomparison operators:')           #comparison operators(<,>,<=,>=,==)
print('\nless ',n1<n2,'\nmore ',n1>n2,'\nequal ',n1==n2,'\nless equal',n1<=n2,'\nmore equal ',n1>=n2)

print('\nlogical operators:')              #logical operators
print('\nused in conditions(and , or)')

print('\nbitwise operator:')                 #bitwise operators(and,or,xor,not,left shift,right shift)
print('complements  = ',~n1,' ',~n2)
print('\nand =',n1&n2,'\nor =',n1|n2,'\nxor =',n1^n2)
print('\nleft shift = ',n1<<n2,'right shift =',n1>>n2)

#single line comment
'''multiline comment'''
