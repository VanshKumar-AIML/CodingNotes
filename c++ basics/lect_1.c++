#include<iostream>
#include<vector>   //vector is a dynamic array
#include<cmath>   //to use math functions
#include<string>

using namespace std;    

namespace f1{
    int x=1;
}

typedef std::vector<std::pair<std::string,int>>pairlist;                    //identifier for vector
typedef std::string text;                                                   //identifier for string

using number=int;                                                           //using keyword(better than typedef)
int calculator();
int nestl();

int main()
{
    //data-types solved
    string s1="hello";                                                      //string 
    bool name=true;
    cout << name << s1;
    const double PI=3.14159;                                                //becomes read only
    double radius =10;
    double circumference=2*PI*radius;
    cout<<circumference;
    cout<<f1::x;                        //namespace required
    pairlist list={};                   //new identifier is used
    text name1="person";
    int f=10;
    cout << float(f);                   //explicit type conversion
    
    //math library functions
    cout << sqrt(9) << pow(2,4);                     //root of 9, 2 power 4
    cout << abs(-4);                                  //always return positive value
    cout << round(3.45) << ceil(4.4) << floor(4.99);    //round used to approximate,ceil for upper value and floor for lower value
    calculator();
    
    //ternary operator
    int n3;
    cout<<"\nenter a number:";
    cin>>n3;
    n3%2==0? cout<<"even" :cout<<"odd";

    /*string methods
    text str1;
    cout<<"\nenter your name:";
    getline(cin,str1);
    if(str1.length() > 12)  
        cout<<"not allowed";
    else
        cout<<str1; */

    cout<<"\n";
    nestl();

    return 0;
}

int calculator()                        //switch case calcular
{
    char op;
    double n1,n2;
    cout <<"\n*********calculator**********\n";
    cout <<"enter operator(+,-,*,/,%,^):";
    cin>>op;
    cout <<"\nenter 1st number:";
    cin>>n1;
    cout<<"\nenter 2nd number:";
    cin>>n2;
    cout<<"\n";
    switch(op)
    {
        case '+':
                cout<<"add = "<<n1+n2;
                break;
        case '-':
                cout<<"sub = "<<n1-n2;
                break;
        case '*':
                cout<<"mul ="<<n1*n2;
                break;
        case '/':
                cout<< "div= "<<n1/n2;
                break;
        case '%':
                cout<<"remainder ="<<int(n1)%int(n2);       //type conversion is done as this function only works for int datatype
                break;
        case '^':
                cout<<"power ="<<pow(n1,n2);
                break;
        default:
                cout<<"wrong operator";    
                break;
    }
}

int nestl()  //nested loops for matrix/pattern 
{
    int x,y;
    cout<<"enter number of rows:";
    cin>>x;
    cout<<"enter number of columns:";
    cin>>y;
    cout<<"\nMatrix:";
    for(int i=1;i<=x;i++){
        for(int j=1;j<=y;j++)
            cout<<"\t"<<i;
        cout<<"\n";
    } 
}