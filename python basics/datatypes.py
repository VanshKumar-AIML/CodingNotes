#data structure operations

def string():                               
    s1='hello'+"world"+'''@@@'''          #concatenation
    l=len(s1)                             #finding length
    print(l,s1)

def list():                                
    print('list:')
    a=[]

def tuple():
    print('tuple:')
    a=()

def set():
    print('set:')
    a={}

def dictionary():
    print('dictionary:')
    a={'key':'value'}

def choice():
    n=1
    while(n!=0):
        print('1.String\n2.List\n3.Tuple\n4.Set\n5.Dictionary\n6.Exit')
        c=int(input('Enter a choice:'))
        if(c==1):
            string()
        elif(c==2):
            list()
        elif(c==3):
            tuple()
        elif(c==4):
            set()
        elif(c==5):
            dictionary()
        elif(c==6):
            print('Exiting>>>>>>>>>>>>>>>>>>')
            break
        else:
            print('Wrong choice')
    
choice()