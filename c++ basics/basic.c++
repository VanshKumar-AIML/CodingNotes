#include <iostream>
using namespace std;  //do  not work for string inputs

int sum(int a,int b);  //function declaration
int fact(int n);
int fib(int f);
int main()
{
    int x,a,b,n,f;
    re:              // label to use goto 
    cout << "enter a number:"; 
    cin >> x;       
    if (x<=12){
        for(int i=1;i<=10;i++){
        cout << x << " *  " << i << " = " << x * i << endl;
            }
        }
    else{
        cout << "this code is only for tables till 12 \n";
        goto re;     //goes to label
    }
    cout << "enter two number:";
    cin >> a >> b;
    cout << sum(a,b);          //calling function

    cout << "\nenter a number:";
    cin >> n;
    cout << "factorial of the number = " << fact(n);
    cout << "\nenter number of terms:";
    cin >> f;
    cout << "\nterms are:";
    for(int i=1;i<=f;i++)      //function called in for loop
    {
        cout << "\n" << fib(i);
    }
    return 0;
}

int sum(int a,int b)       //function
{    
    return a+b;
}

int fact(int n)          //recursive function
{
    if (n==0 || n==1)    //base case condition
      return 1;
 return n*fact(n-1); 
}
int fib(int f){        //fabonacci
    if (f==1)
     return 0;
    else if(f==2 || f==3)
     return 1;
return fib(f-1) + fib(f-2);
}

// <= single line comments
/*  <=  multi-line comments   =>*/