import java.util.Scanner;   //library for input

public class l_1 {            //complete body(here body name is file name)

    static int var=4;        // -> global declaration

    public static void main(String[] args){      //function -> write main then enter(shortcut)

        int a=5;                   //variablle declaration
                                   //(double,string,char,boolean,int) 
        
        System.out.print("hello world\n");            //simple print
        System.out.println("new line of code");     //print with new line    -> write sout then enter(shortcut)
        System.out.printf("similar to c language -> %d",a);    //formatted print with  [format specifiers (%d,%f,%lf,%c,%s) ]

        System.out.println(a);                        //variable printing
        System.out.println("a");                    //it will print variable as string

        String name="Vansh";
        System.out.println("Hello "+name);      //string concatenation
    
        Scanner scanner = new Scanner(System.in);  //now scanner is used to take input

        System.out.print("Enter your email:");    //to take input
        String email= scanner.nextLine();
        System.out.println("Your email is " + email);

        if(a==5)                              //conditional statements are same
        {
            System.out.println("true condition");
        }
        else
        {
            System.out.println("false");
        }
    
        scanner.close();

        fun(args);                            // function called
        
        for(int i=0;i<=10;i++){
            System.out.print("\n"+i);
        }
    
    
    }                                                 

    public static void fun(String[] args){            //new function
        System.out.println("new function");
    }
}

/* *******************************************************Extra notes***************************************************** */


/* multiline comment */


/* ***********************constructs used in java****************** */
/* 
 *while and do-while loops exist
 * all if-else  and switch case work 
 * 
 * for each loop
 * for(int num:array){
 *                      System.out.println(num);
 *              }
 * 
 *  all other statements work same
 *  (input,output and function)
 *  
 */

 //(printf also exist) -> with %d,%f,%C,%b(boolean) as format specifiers

 
 /* *********************String methods**************************** */

 // c-character

 //string mathods- str.length(),str.charAt(index),str.indexof("c"),str.lastIndexOf("c")
 //str.toLowercase(),str.toUppercase(),str.trim() ->trim is used to remove empty spaces across a string
 //str = str.replace("to change","changed to")
 //substr=str.substring(initial,final)  -> to get a part of the main string from initial index to final index

 //Multiline string:
 //  String str_name="""
 //
 //                         """ 

 //Ternary operator    datatype variable=(condition)? expression 1(True): expression 2(False);


/* *******************************Extra************************************ */

/*Scanner can be used as a parameter in a function
   function(args,scanner_name)          ->function call
   
   static void function_name(datatype[],Scanner scanner_name){

                       ( block of code )
   
        }
  */