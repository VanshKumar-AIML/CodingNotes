import java.util.Scanner;
import java.util.Random;

public class l_4 {

    public static void main(String[] args) {        //main body
        ch(args);
    }

    static void ch(String [] args)                  //choices
    {
        Scanner input=new Scanner(System.in);
        int c;
        
        do{
            System.out.println("Programs:");
            System.out.println("1.dice roller");
            System.out.println("2.quiz game");
            System.out.println("3.Slot machine");
            System.out.println("4.Exit");

            System.out.print("Enter a choice:");
            c=input.nextInt();

            switch(c)
            {
                case 1:
                    dr(args,input);
                    break;
                case 2:
                    qg(args,input);
                    break;
                case 3:
                    sm(args,input);
                    break;
                case 4:
                    System.out.println("Exiting>>>>>>>>>");
                    break;
                default:
                    System.out.println("Wrong choice,try again");
            }
        } while(c!=4);
        input.close();
    }

    static void dr(String[] args,Scanner input)             //dice roller
    {
        Random rand=new Random();
        System.out.print("Enter the number of dice to roll:");
        int num=input.nextInt();
        int t=0;

        if(num>0)
        {
            
            for(int i=0;i<num;i++)
            {
                int r=rand.nextInt(1,7);
                pd(r);
                System.out.println("You rolled:"+r);
                t+=r;
            }
            System.out.println("Total:"+t);
        }
        else
            System.out.println("Wrong choice");
    }
    static void pd(int r)                                   //ascii art of dice
    {

        String dice1="""              
                 -------
                |       |
                |   ●   |
                |       |
                 -------
                """;
        String dice2="""
                 -------
                | ●     |
                |       |
                |     ● |
                 -------
                """;
        String dice3="""
                 -------
                |●      |
                |   ●   |
                |      ●|
                 -------
                """;
        String dice4="""
                 -------
                |●     ●|
                |       |
                |●     ●|
                 -------
                """;
        String dice5="""
                 -------
                | ●   ● |
                |   ●   |
                | ●   ● |
                 -------
                """;
        String dice6="""
                 -------
                | ●   ● |
                | ●   ● |
                | ●   ● |
                 -------
                """;

        switch(r)
        {
            case 1 -> System.out.print(dice1); 
            case 2 -> System.out.println(dice2);
            case 3 -> System.out.println(dice3);
            case 4 -> System.out.println(dice4);
            case 5 -> System.out.println(dice5);
            case 6 -> System.out.println(dice6);
        }

        
    }

    static void qg(String[] args,Scanner input)            //quiz game
    {
        String[] q={"1.What year c++ created?:",                  //questions
                "2.Who invented c++?:",
                "3.c++ is also written?:"};

        String [][] op={{"1.1985","2.1989","3.1975","4.1969"},    //for options
                    {"1.Guido","2.Bjarne","3.John","4.Joseph"},
                    {"1.cp+","2.cpp","3.c+-","4.c+++"}};

        int [] answer={1,2,2};                              //answer options
        int ans;
        int sc=0;

        for(int i=0;i<q.length;i++)
        {
            System.out.println(q[i]);

            for (String ops : op[i])
            {
                System.out.println(ops);
            }

            System.out.print("Enter the option:");
            ans=input.nextInt();

            if(ans== answer[i])
                System.out.println("Correct answer");
            else
                System.out.println("Wrong");

            sc++;
        }

        System.out.printf("\nFinal score is %d out of %d\n.",sc,q.length);
       
    }
   
    static void sm(String[] args,Scanner input)            //slot machine
    {
        int balance=100;
        int bet;
        int payout;
        String[] row;
        String play;

        System.out.println("   Welcome to java slots   \n");
        System.out.println("Symbols: 1 2 3 4 5\n");

        while(balance>0){
            System.out.printf("current balance = %d.\n",balance);
            System.out.print("enter bet amount:");
            bet=input.nextInt();
            input.nextLine();

            if(bet>balance){
                System.out.println("Not enough balance");
                continue;
            }
            else if(bet<=0){
                System.out.println("Must be greater than 0");
                continue;
            }
            else{
                balance -= bet;
                System.out.println("remaining balance:"+balance);
            }
            System.out.println("Spinning>>>>>");
            row=spinr();
            pr(row);
            payout=gp(row,bet);

            if(payout>0){
                System.out.println("You won "+payout);
                balance += payout;
            }
            else{
                System.out.println("You lost!");
            }

            System.out.print("Want to play again?(Y/N):");
            play=input.nextLine().toUpperCase();

            if(!play.equals("Y")){
                break;
            }
        }

        System.out.println("GAME over! final balance= "+balance);
    }
    static String[] spinr(){                               //to spin symbols

        String [] sym= {"1","2","3","4","5"};
        String[] r=new String[3];
        Random rand=new Random();

        for(int i=0;i<3;i++)
        {
            r[i]=sym[rand.nextInt(sym.length)];
        }

        return r;
    }
    static void pr(String[] row)                           //to print the symbols
    {
        System.out.println("**************************");
        System.out.println(" "+String.join(" | ",row));
        System.out.println("**************************");
    }
    static int gp(String[] row,int bet){                   //getting payout(won amount)

        if(row[0].equals(row[1])&&row[1].equals(row[2])){
            return switch(row[0]){
                case "1" -> bet*3;
                case "2" -> bet*4;
                case "3" -> bet*5;
                case "4" -> bet*10;
                case "5" -> bet*20;
                default -> 0;
            };
        }
        else if(row[0].equals(row[1])){
            return switch(row[0]){
                case "1" -> bet*2;
                case "2" -> bet*3;
                case "3" -> bet*4;
                case "4" -> bet*5;
                case "5" -> bet*10;
                default -> 0;
            };
        }
        else if(row[1].equals(row[2])){
            return switch(row[1]){
                case "1" -> bet*2;
                case "2" -> bet*3;
                case "3" -> bet*4;
                case "4" -> bet*5;
                case "5" -> bet*10;
                default -> 0;
            };
        }
        return 0;
    }
   
}
