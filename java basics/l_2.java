import java.util.Scanner;
import java.util.Random;     //to work with random function

public class l_2 {

    public static void main(String[] args)       //main body
    {
       choice(args);
    }


    static void choice(String[] args)    //selection of functions
    {
        Scanner input=new Scanner(System.in);

        int c;
         do {

            System.out.println("\nBasic Programs:\n");
            System.out.println("1. Area of rectangle");
            System.out.println("2. Mad libs game");
            System.out.println("3. Shopping cart");
            System.out.println("4. Random number");
            System.out.println("5. Math library operations");
            System.out.println("6. Exit\n");
            System.out.print("Enter a choice: ");
            c = input.nextInt();

            switch(c) {
                case 1:
                    area(args);
                    break;
                case 2:
                    madlibsgame(args);
                    break;
                case 3:
                    scart(args);
                    break;
                case 4:
                    r(args);
                    break;
                case 5:
                    m(args);
                    break;
                case 6:
                    System.out.println("Exiting................");
                    break;
                default:
                    System.out.println("It is not a valid choice.");
                    break;
            }
        } while(c != 6);  // repeat until user chooses Exit (6)

        input.close();
    }

    static void area(String[] args)      //area of rectangle
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter length of rectangle:");
        Double l=input.nextDouble();
        System.out.print("Enter width of rectangle:");
        Double w=input.nextDouble();

        System.out.println("Area = "+ l*w);
        input.close();
        
    }
    static void madlibsgame(String[] args)    //MAD LIBS GAME
    {
        Scanner input= new Scanner(System.in);

        String adjective1;
        String noun1;
        String adjective2;
        String verb1;
        String adjective3;

        System.out.print("Enter an adjective(description):");
        adjective1=input.nextLine();
        System.out.print("Enter a noun(animal):");
        noun1=input.nextLine();
        System.out.print("Enter an adjective(description):");
        adjective2=input.nextLine();
        System.out.print("Enter a verb(-ing used):");
        verb1=input.nextLine();
        System.out.print("Enter an adjective(description):");
        adjective3=input.nextLine();

        System.out.println("\n");
        System.out.println("Today i went to "+adjective1+" zoo . ");
        System.out.println("In a exhibit,i saw "+noun1+".");
        System.out.println(noun1 +" was "+adjective2+" and "+verb1+" ! ");
        System.out.println("i was "+adjective3+" ! ");

        input.close();
    }
    static void scart (String[] args)       //Shopping cart function
    {
        Scanner input=new Scanner(System.in);
        String item;
        double price;
        int quantity;
        char currency= '$';
        double total;

        System.out.print("what you will buy?: ");
        item=input.nextLine();

        System.out.print("What is the price for each?: ");
        price=input.nextDouble();

        System.out.print("Enter the quantity: ");
        quantity=input.nextInt();

        total=price*quantity;
        System.out.println("your have bought "+quantity+" "+item);
        System.out.print("Total amount : "+currency+total);

        input.close();
    }
    static void r(String[] args)           //random number
    {
        Random rand=new Random();             //keyword for random function is created

        int num = rand.nextInt(1,6);   

        System.out.println("Random number(1-6) is "+num);
    }
    static void m(String[] args)           //math library operations
    {

       System.out.println(Math.PI+Math.E);        //to use math constants
       System.out.println(Math.pow(2,3));    //8.0
       System.out.println(Math.sqrt(9));       //3.0
       System.out.println(Math.abs(-3));         //3(always +ve)
       System.out.println(Math.round(3.14));   //3(approximate)
       System.out.println(Math.ceil(8.1));     //9.0(above int)
       System.out.println(Math.floor(4.99));   //4.0(lower int)
       System.out.println(Math.max(2,3));    //3
       System.out.println(Math.min(3,4));    //3

    }

}

//using static instead of public static also works(methods)

