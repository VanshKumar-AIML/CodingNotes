#include <iostream>
using namespace std;

//_____________________________________________________________________________________________________
// Lecture - 1
//_____________________________________________________________________________________________________

/*
int smallest(int arr[]);
void printSquare(int n);
void printTriangle(int n);
void printRtriangle(int n);
void printDiamondPattern(int n);

int main()
{
    int arr[]={6,2,3,4,5},n;
    cout << smallest(arr) << "\n";
    cout << "enter number of rows:"; 
    cin >> n;
    cout << "square" << endl;
    printSquare(n);
    cout << "triangle";
    printTriangle(n);
    cout << "side triangle";
    printRtriangle(n);
    cout << "diamond pattern" << endl;
    printDiamondPattern(n);
    return 0;
}

int smallest(int arr[])                 //single responsibility principle
{
    int min =arr[0];
    for(int i=0;i<5;i++)
        if(arr[i]<min)
            min = arr[i];
    return min;
}

void printSquare(int n)
{
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            cout << "*" ;
        }
        cout << endl;                    //for new line(more readable)
    }
}

void printTriangle(int n)
{
    for(int i=0; i<=n; i++)
    {
        for(int j=0; j<=n; j++)
        {
            if(i>j)
                cout << "*";
        }
        cout << endl;
    }
}

void printRtriangle(int n)
{
    for(int i=0; i<=n; i++)
    {
        for(int j=i; j<=n; j++)
        {
                cout << " ";
        }
        for(int k=0;k<i;k++)
        {
            cout << "*";
        }
        cout << endl;
    }
}

void printDiamondPattern(int n) {
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            cout << "*";
        }
        cout << endl;
    }

    for (int i = n - 1; i >= 1; i--) {
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        for (int j = 1; j <= 2 * i - 1; j++) {
            cout << "*";
        }
        cout << endl;
    }
}

*/

//_____________________________________________________________________________________________________
//lecture - 2
//_____________________________________________________________________________________________________

/*
int printArray(int *arr, int n, char seperator=' ')       // seperator key word (to use a character)
{
    for(int i=0; i<n; i++)
        cout << arr[i] << seperator;
}

int ReverseArray(int *arr,int n, char seperator=' ')
{
    for(int i=n-1; i>-1; i--)   
        cout << arr[i] << seperator;
}

int main()
{
    int n=4;
    int arr[4]={1,2,3,4};

    printArray(&arr[0], n);
    cout << endl;
    ReverseArray(&arr[0], n);
    cout << endl;
    return 0;
}
*/

//_____________________________________________________________________________________________________
//lecture - 3
//_____________________________________________________________________________________________________

/*
int zpattern(int n)
{
    for(int i=0;i<n;i++)
    {
        for(int j=0; j<n; j++)
            {
                if(i==0 || i==(n-1) || i==(n-j))
                    printf("*");
                else 
                    printf(" ");
            }
        printf("\n");
    }
}

int window()
{
    int arr[]={1,2,3,4,5};
    int n=sizeof(arr)/sizeof(arr[0]);
    int sum,max=0;

    for(int i=0; i<n-2; i++)
    {
        sum=0;
        for(int j=i; j<i+3; j++)
            sum += arr[j];
        cout << sum << endl;
        if(sum>=max)
            max=sum;
    }
    cout << max << endl;
}

int fact(int n)
{
    if(n<=1)
        return 1;
    return n*fact(n-1);
}

// write a program to print n to 1 numbers by using recursion ?
int count(int n)
{
    if(n==1)
        return 1;
    cout << n << "\t";
    return count(n-1);
}

int main()
{
    // zpattern(11);
    window();
    cout << fact(5) << endl;
    cout << count(5);
}
*/

//______________________________________________________________________________________________________
//lecture - 4
//______________________________________________________________________________________________________

/* */