#include<iostream>
#include<ctime>         //random events per time
using namespace std;

int c1();               //functions called
    int r();
        int c2();
            int randomnumber();
            int dice3();
            int revent();
    int game();

int main()              //main area
{
    cout<<"program working with random:\n";
    c1();
    return 0;
}

int c1()                 //choice between random and game
{
    int c;
    cout<<"enter choice(Random(1)/Game(2)):";
    cin>>c;
    switch(c)
    {
        case 1:
            r();
            break;
        case 2:
            game();
            break;
        default:
            cout<<"not a choice";
            break;
    }
}

int r()
{
    c2();
    return 0;
}

int c2()           //choice inside random
{
    int c;
    cout<<"random number generator(1)\n3-dice(2)\n";
    cout<<"random event(3):";
    cout<<"\nenter choice(1/2/3):";
    cin>>c;
    switch(c)
    {
        case 1:
            randomnumber();
            break;
        case 2:
            dice3();
            break;
        case 3:
            revent();
            break;
    }
}

int randomnumber()
{
    //psedo random
    int n=rand();            //random number upto(0 - 32k)
    cout << n;
    int n1=(rand() % 6)+1;         //random number upto(1-6)
    cout<< "\n" << n1;
}

int dice3()
{
    int n1=(rand() % 6)+1;
    int n2=(rand() % 6)+1;
    int n3=(rand() % 6)+1;
    cout<<n1<<"\t"<<n2<<"\t"<<n3; //combination of the 3 dice
}

int revent()
{
    int gn;
    srand(time(0));
    int r=rand()%5 + 1;
    cout<<"enter a guess number(1-5):";
    cin>>gn;
    if(gn==r)
        cout<<"\nsame number\n";
    else
        cout<<"different number\n";
    switch(r)
    {
        case 1:
            cout<<"winner";
            break;
        case 2:
            cout<<"winner 2";
            break;
        case 3:
            cout<<"average";
            break;
        case 4:
            cout<<"below 4";
            break;
        case 5:
            cout<<"loser";
            break;
    }
}

int game()                   //number guessing game
{
    int c,gn;
    c=rand()%10 +1;
    cout<<"\n******************************Number guessing game**********************\n";
    cout<<"\nyou have three chances:\n";
    for(int i=0;i<3;i++){
        cout<<"\nguess a number(0-10):";
        cin>>gn;
        if(gn>c)
            cout<<"too high\n";
        else if(gn==c)
            cout<<"winner\n";
        else
            cout<<"too low\n";
        c=rand()%10+1;
    }
    cout<<"\nif 2 choices are correct winner\n";
    cout<<"\n***************************************************************************\n";
    return 0;
}