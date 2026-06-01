import java.util.Scanner;

public class tt {
    public static void main(String [] args)
    {
        Scanner input = new Scanner(System.in);

        System.out.print("enter number of rows:");
        int n=input.nextInt();

        System.out.println("Square pattern");
        printSquare(n);
        System.out.println("different pattern");
        printdifferent(n);
        System.out.println("Practice pattern");
        practicepattern(n);

        input.close();
    }

    static void printSquare(int n)
    {
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<n; j++)
                System.out.print("*");
            System.out.println("");
        }
    }

    static void printdifferent(int n)
    {
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<n; j++){
                if(i>j)
                    System.out.print("*");
                System.out.print(" ");
            }

            for(int j=0; j<n; j++){
                if(j>i)
                    System.out.print("*");
                System.out.print(" ");
            }
        }
    }

    static void practicepattern(int n)
    {
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<=i;j++)
            {
                System.out.printf("%d  ",i-j+1);
            }
        System.out.println("");
        }
    }
}
