#include<iostream>
#include<ctime>        //for random function

using namespace std;

int choice();
    void bank();
        void showBalance(double balance);           //functions declared as per datatypes
        double deposit();
        double withdraw(double balance);

    void rps();                                     //rock paper scissor game
        char userc();
        char compc();
        void showc(char c);
        void winner(char p,char c);

    void ttt();                                     //tic tac toe game functions
        void drawb(char *sp);
        void pmove(char *sp,char pla);
        void cmove(char *sp,char com);
        bool win(char *sp,char pla,char com);
        bool tie(char *sp,char pla,char com);

int main()                                     //main body
{
    choice();
}

int choice()
{
    int c;
    do{
        cout<<"These are random projects:\n";
        cout<<"1.Bank system\n2.Rock-paper-scissor game\n";
        cout<<"3.tic tak toe game\n";
        cout<<"\nenter a choice:";
        cin>>c;
        switch(c){
            case 1:
                bank();
                break;
            case 2:
                rps();
                break;
            case 3:
                ttt();
                break;
            case 4:
                cout<<"\nthanks for visiting\n";
                break;
            default:
                cout<<"\nInvalid choice\n";
                break;
        }
    } while(c!=4);
}

void bank()
{
    double balance=0;
    int c;
   do{
    cout<<"************ Bank system **************\n";
    cout<<"1.Show balance\n";
    cout<<"2.Deposit money\n";
    cout<<"3.Withdraw money\n";
    cout<<"4.exit\n";
    cout<<"enter your choice:";
    cin>>c;

    cin.clear();        //clear the screen 
    fflush(stdin);      //for invalid choose
    cout<<"\n";
    switch(c)
    {
        case 1:
            showBalance(balance);
            break;
        
        case 2:
            balance += deposit();
            break;
        
        case 3:
            balance -= withdraw(balance);
            break;
        case 4:
            cout<<"thanks for visiting\n";
            break;
        default:
            cout<<"not a valid choice";
            break;
    }
   } while(c!=4);

}
void showBalance(double balance)
{
    cout<<"your balance is: "<<balance<<"\n";
}
double deposit()
{
    double a=0;
    cout<<"add deposit amount:";
    cin>>a;
    if(a<0)
        return 0;
    return a;
}
double withdraw(double balance)
{
    double w;
    cout<<"add withdraw amount:";
    cin>>w;
    if(w>balance)
    {
        cout<<"insufficient balance\n";
        return 0;
    }
    else if(w<0)
    {
        cout<<"Not a withdraw\n";
        return 0;
    }
    else
        return w;
}

void rps()
{
    char pla,com;

    pla=userc();
    cout<<"\nyour choice is:";
    showc(pla);

    com=compc();
    cout<<"\ncomputer choice is:";
    showc(com);

    cout<<"\n";

    winner(pla,com);

}
char userc()
{
    char p;
    do
    {
        cout<<"\nRock paper scissor game\n";
        cout<<"r for rock\n";
        cout<<"p for paper\n";
        cout<<"s for scissors\n";
        cout<<"enter a choice:";
        cin>>p;
    } while (p!='r'&&p!='p'&&p!='s');
    cout<<"\n";
    return p;
}
char compc()
{
    int i= rand()%3 + 1;

    switch(i)
    {
        case 1:
            return 'r';
        case 2:
            return 'p';
        case 3:
            return 's';
    }

}
void showc(char c)
{
    switch(c)
    {
        case 'r':
            cout<<"rock";
            break;
        case 'p':
            cout<<"paper";
            break;
        case 's':
            cout<<"scissors";
            break;
    }
}
void winner(char p,char c)
{
    switch(p)
    {
        case 'r':
            if(c=='r')
                cout<<"it is a tie";
            else if(c=='p')
                cout<<"you lose";
            else
                cout<<"you win";
            break;
        case 'p':
            if(c=='r')
                cout<<"you win";
            else if(c=='p')
                cout<<"it is a tie";
            else
                cout<<"you lose";
            break;
        case 's':
            if(c=='r')
                cout<<"you win";
            else if(c=='p')
                cout<<"you lose";
            else
                cout<<"it is a tie";
            break;
    }
}

void ttt()
{
    char spa[9]={' ',' ',' ',' ',' ',' ',' ',' ',' '};
    char pla='O';
    char com='X';
    bool running = true;
    cout<<"\n________________________________________________________\n";
    cout<<"\nTic tac toe game\n";
    drawb(spa);
    cout<<"\n";
    while(running)
    {
        pmove(spa,pla);
        drawb(spa);
        if(win(spa,pla,com))
        {
            running=false;
            break;
        }
        else if(tie(spa,pla,com))
        {
            running=false;
            break;
        }

        cmove(spa,com);
        drawb(spa);
        if(win(spa,pla,com))
        {
            running=false;
            break;
        }
        else if(tie(spa,pla,com))
        {
            running=false;
            break;
        }
        
    }
    cout<<"\n*************************************************\n";
    cout<<"\ngame over\n";
}
void drawb(char *sp)  //to make grid for the board
{
    cout<<"\n";
    cout<<"     |     |     "<<"\n";
    cout<<"  "<<sp[0]<<"  |  "<<sp[1]<<"  |  "<<sp[2]<<"   "<<"\n";
    cout<<"_____|_____|_____"<<"\n";
    cout<<"     |     |     "<<"\n";
    cout<<"  "<<sp[3]<<"  |  "<<sp[4]<<"  |  "<<sp[5]<<"   "<<"\n";
    cout<<"_____|_____|_____"<<"\n";
    cout<<"     |     |     "<<"\n";
    cout<<"  "<<sp[6]<<"  |  "<<sp[7]<<"  |  "<<sp[8]<<"   "<<"\n";
    cout<<"     |     |     "<<"\n";
    cout<<"\n";
}
void pmove(char *sp,char pla)                        //for player move
{
    int num;
    do{
        cout<<"enter a number for marker(1-9):";
        cin>>num;
        num--;
        if(sp[num]==' ')
        {
            sp[num]= pla;
            break;
        }
    } while(!num>0 || !num<8);
}
void cmove(char *sp,char com)                       //computer move by random function
{
    int num;
    
    while(true)
    {
        num=rand()%9;
        if(sp[num]==' ')
        {
            sp[num]=com;
            break;
        }
    }
}
bool win(char *sp,char p,char c)                                //to declare winner
{
    if((sp[0]!=' ')&&(sp[0]==sp[1])&&(sp[1]==sp[2]))      //checking same across rows
    {
        sp[0]==p ? cout<<"You win!" : cout<<"You lose!";
    }
    else if((sp[3]!=' ')&&(sp[3]==sp[4])&&(sp[4]==sp[5]))
    {
        sp[3]==p ? cout<<"You win!" : cout<<"You lose!";
    }
    else if((sp[6]!=' ')&&(sp[6]==sp[7])&&(sp[7]==sp[8]))
    {
        sp[6]==p ? cout<<"You win!" : cout<<"You lose!";
    }
    else if((sp[0]!=' ')&&(sp[0]==sp[3])&&(sp[3]==sp[6]))  //checking same across columns
    {
        sp[0]==p ? cout<<"You win!" : cout<<"You lose!";
    }
    else if((sp[1]!=' ')&&(sp[1]==sp[4])&&(sp[4]==sp[7]))
    {
        sp[1]==p ? cout<<"You win!" : cout<<"You lose!";
    }
    else if((sp[2]!=' ')&&(sp[2]==sp[5])&&(sp[5]==sp[7]))
    {
        sp[2]==p ? cout<<"You win!" : cout<<"You lose!";
    }
    else if((sp[0]!=' ')&&(sp[0]==sp[4])&&(sp[4]==sp[8]))  //checking same across diagonals
    {
        sp[0]==p ? cout<<"You win!" : cout<<"You lose!";
    }
    else if((sp[2]!=' ')&&(sp[2]==sp[4])&&(sp[4]==sp[6]))
    {
        sp[2]==p ? cout<<"You win!" : cout<<"You lose!";
    }
    else 
        return false;
    
    return true;
}
bool tie(char *sp,char p,char c)
{
    for(int i=0;i<9;i++)
    {
        if(sp[i]== ' ')
        {
            return false;
        }
    }
    cout<<"it is tie\n";
    return true;
}