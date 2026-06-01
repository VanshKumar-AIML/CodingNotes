#include<iostream>

using namespace std;

int choice();                                        //function declaration
    int filler();  

    void quiz();

    int ccv();                            //credit card validation
        int getd(const int num);
        int sumodd(const string cnum);
        int sumeven(const string snum);

int main()
{
    choice();
    return 0;
}

int choice()
{
    int c;
    cout<<"1.filler operation\n2.quiz game\n";
    cout<<"3.Credit card validation\n";
    cout<<"4.Exit";
    cout<<"enter a choice:";
    cin>>c;
    switch(c){
        case 1:
            filler();
            break;
        case 2:
            quiz();
            break;
        case 3:
            ccv();
            break;
        case 4:
            cout<<"thanks for visiting";
            break;
        default:
            cout<<"not a choice";
            break;
    }
}

int filler()
{
    string elements[15];
    fill(elements,elements+15,"elements");          //to fill same elements
    for(int i=0;i<15;i++)                           //fill(begin,begin+end,element);
    {                                               //in begin write object name
        cout<<"\n"<< elements[i];
    }
}

void quiz()
{
    string q[]={"1.What year c++ created?:",                  //questions
                "2.Who invented c++?:",
                "3.c++ is also written?:"};

    string op[][4]={{"A.1985","B.1989","C.1975","D.1969"},    //for options
                    {"A.Guido","B.Bjarne","C.John","D.Joseph"},
                    {"A.cp+","B.cpp","C.c+-","D.c+++"}};

    char answer[]={'A','B','B'};                              //answer options
    
    int size=sizeof(q)/sizeof(q[0]);
    char guess;
    int score=0;

    for(int i=0;i<size;i++)
    {
        cout<<"\nquestions\n";
        cout<<q[i]<<"\n";

        for(int j=0;j<sizeof(op[i])/sizeof(op[i][0]);j++)
        {
            cout<< op[i][j]<<"\n";
        }

        cout<<"\nEnter option:";
        cin>>guess;
        guess=toupper(guess);

        if(guess==answer[i])
        {
            cout<<"CORRECT\n";
            score++;
        }
        else
        {
            cout<<"wrong\n";
            cout<<"answer"<<answer[i]<<"\n";
        }
    }
    cout<<"\nResults\n";
    cout<<"correct answers:"<<score<<"\n";
    cout<<"total questions:"<<size<<"\n";
    cout<<"Score:"<<(float(score)/float(size))*100<<"%";
}

//to check validation of a credit card number

/*Luhn algorithm is used in following steps
  1.Double every second digit from right to left
    If doubled number is 2 digit,split them 
  2.Add all single digits from step 1
  3.Add all odd numbered digits from right to left
  4.Sum results from steps 2 and 3
  5.If step 4 is divisible by 10(valid)

  example:6011 0009 9013 9424
          6 1  0 0  9 1  9 2  only even index taken
        1 2 2  0 0 1 8 2 1 8 4     doubled and splitted
        1+2+2+1+8+2+1+8+4=29(sum)
         6011 0009 9013 9424
          0 1  0 9  0 3  4 4  only odd index taken
          0 2  0 1 8  6  8 8  double and split
          21(sum)
          21+29=50 if (50%10==0) then valid         */

int ccv()
{
    string cnum;
    int result=0;

    cout<<"enter credit card number:";
    cin>>cnum;

    result=sumeven(cnum)+sumodd(cnum);

    if(result%10==0)
        cout<<cnum<<"- valid card number";
    else
        cout<<cnum<<" not valid";
    
}

int getd(const int num)
{
    return num%10 +(num/ 10 % 10);  //sum of double digit
}

int sumeven(const string cnum)
{
    int sum=0;
    for(int i=cnum.size()-2;i>=0;i-=2)
        sum+=getd((cnum[i]-'0')*2);         //to maintain overhead

        return sum;
}

int sumodd(const string cnum)
{

    int sum=0;
    for(int i=cnum.size()-1;i>=0;i-=2)
        sum+=cnum[i]-'0';         //to maintain overhead

        return sum;
}