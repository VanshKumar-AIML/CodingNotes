import java.util.Scanner;

public class l_3 {
    
    public static void main(String[] args)              //main body
    {
       choice(args);
    }


    static void choice(String[] args) {         //choice body
        Scanner input=new Scanner(System.in);
        int c;
        do{
            System.out.println("practice programs:");
            System.out.println("1.Multiplication table");
            System.out.println("2.Temperature converter");
            System.out.println("3.Weight converter");
            System.out.println("4.Compound interest calculator");
            System.out.println("5.Exit");
            System.out.print("Enter a choice:");
            c=input.nextInt();
            switch(c){
                case 1:
                    mtab(args,input);
                    break;
                case 2:
                    tempc(args,input);
                    break;
                case 3:
                    weightc(args,input);
                    break;
                case 4:
                    cic(args,input);
                    break;
                case 5:
                    System.out.println("Exiting.................................");
                    System.out.println("thanks for visiting");
                    break;
                default:
                    System.out.println("Wrong choice try again");
            }

        } while(c!=5);
        input.close();
    }
    
    static void mtab(String [] args,Scanner input){
        System.out.print("Enter a number:");
        int a=input.nextInt();
        System.out.println("Multiplication table is:");
        for(int i=1;i<11;i++)
        {
            System.out.printf("%d * %d = %d\n",a,i,a*i);      //using printf same as c language
        }
    }
    static void tempc(String[] args,Scanner input) {             //temperature converter
        int c;
        do{
            System.out.println("Temperature conversions:");
            System.out.println("1.C -> F");
            System.out.println("2.F -> C");
            System.out.println("3.Exit\n");
            System.out.print("Enter a choice:");
            c=input.nextInt();
            System.out.print("Enter the temperature:");
            double t=input.nextDouble();

            switch(c){
                case 1:
                    System.out.println("In F is "+t*33.8);
                    break;
                case 2:
                    System.out.println("In C is "+t/33.8);
                    break;
                case 3:
                    System.out.println("Exiting>>>>>>>>>>>>>>");
                    break;
                default:
                    System.out.println("wrong choice -> try again");
            }
        } while(c!=3);
    }
    static void weightc(String[] args,Scanner input) {           //weight converter
        int c;
        do{

            System.out.println("Weight conversions:");  
            System.out.println("1.kgs to lbs(pounds)");
            System.out.println("2.lbs(pounds) to kgs");
            System.out.println("3.Exit\n");
            System.out.print("Enter a choice:");
            c=input.nextInt();    
            System.out.println("Enter the weight:");
            double w=input.nextDouble();

            switch (c) {
                case 1:
                    System.out.println("In lbs "+w*2.2046);
                    break;
                case 2:
                    System.out.println("In kgs "+w/2.2046);
                    break;
                case 3:
                    System.out.println("Exiting>>>>>>>>>>>>>>>>>>>");
                    break;
                default:
                    System.out.println("Wrong choice try again");
            }
           
        } while(c!=3);
    }
    static void cic(String[] args,Scanner input) {              //compound interest calculator
        double r=9.5;
        double n=2;
        System.out.print("Enter the principle amount:");
        double p=input.nextDouble();
        System.out.println("Enter the time required(in years):");
        double t=input.nextDouble();

        double ci= p*Math.pow(r/n,t*n);

        System.out.printf("Compound interest at the rate of 9.5% is %lf ",ci);
        System.out.println("compounded every 6 months");
    }

}
