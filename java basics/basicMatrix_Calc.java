import java.util.Scanner;

public class basicMatrix_Calc {
    
    //main body(all the functions come here and execute)
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        menu(input);
        input.close();
    }

    //To choose an OPERATIONS of matrix

    static void menu(Scanner input) {                     
        int choice;
        do {
            System.out.println("\nMatrix Calculator");

            System.out.println("1. Add");
            System.out.println("2. Subtract");
            System.out.println("3. Multiply");
            System.out.println("4. Inverse (2x2 only)");
            System.out.println("5. Determinant (2x2 only)");
            System.out.println("6. Exit\n");

            System.out.print("Choose an operation: ");
            choice = input.nextInt();

            switch (choice) {
                case 1:
                    Double[][] a1 = inputMatrix(input, "Matrix A");
                    Double[][] b1 = inputMatrix(input, "Matrix B");
                    display(add(a1, b1), "Addition Result");
                    break;
                case 2:
                    Double[][] a2 = inputMatrix(input, "Matrix A");
                    Double[][] b2 = inputMatrix(input, "Matrix B");
                    display(subtract(a2, b2), "Subtraction Result");
                    break;
                case 3:
                    Double[][] a3 = inputMatrix(input, "Matrix A");
                    Double[][] b3 = inputMatrix(input, "Matrix B");
                    display(multiply(a3, b3), "Multiplication Result");
                    break;
                case 4:
                    Double[][] a4 = inputMatrix(input, "Matrix");
                    display(inverse2x2(a4), "Inverse Result");
                    break;
                case 5:
                    Double[][] a5 = inputMatrix(input, "Matrix");
                    System.out.printf("Determinant: %.2f\n", determinant2x2(a5));
                    break;
                case 6:
                    System.out.println("Exiting Matrix Calculator.................................");
                    System.out.println("Thanks for visiting");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 6);
    }

    //INPUT AND OUTPUT OPERATIONS

    static Double[][] inputMatrix(Scanner input, String name) {        
        System.out.print("Enter rows and columns for " + name + ": ");
        int r = input.nextInt();
        int c = input.nextInt();
        Double[][] mat = new Double[r][c];
        System.out.println("Enter elements of " + name + ":");
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                mat[i][j] = input.nextDouble();
        return mat;
    }

    static void display(Double[][] mat, String name) {               
        System.out.println(name + ":");
        for (Double[] row : mat) {
            for (Double val : row)
                System.out.printf("%.2f\t", val);
            System.out.println();
        }
    }

    //OPERATIONS OF MATRIX

    static Double[][] add(Double[][] a, Double[][] b) {                 
        int r = a.length, c = a[0].length;
        Double[][] result = new Double[r][c];
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                result[i][j] = a[i][j] + b[i][j];
        return result;
    }
    static Double[][] subtract(Double[][] a, Double[][] b) {
        int r = a.length, c = a[0].length;
        Double[][] result = new Double[r][c];
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                result[i][j] = a[i][j] - b[i][j];
        return result;
    }
    static Double[][] multiply(Double[][] a, Double[][] b) {
        int r1 = a.length, c1 = a[0].length;
        int r2 = b.length, c2 = b[0].length;
        if (c1 != r2) {
            System.out.println("Matrix dimensions incompatible for multiplication.");
            return new Double[0][0];
        }
        Double[][] result = new Double[r1][c2];
        for (int i = 0; i < r1; i++)
            for (int j = 0; j < c2; j++) {
                result[i][j] = 0.0;
                for (int k = 0; k < c1; k++)
                    result[i][j] += a[i][k] * b[k][j];
            }
        return result;
    }
    static Double[][] inverse2x2(Double[][] mat) {
        if (mat.length != 2 || mat[0].length != 2) {
            System.out.println("Only 2x2 matrices supported for inverse.");
            return new Double[0][0];
        }
        double det = determinant2x2(mat);
        if (det == 0) {
            System.out.println("Matrix is singular, inverse doesn't exist.");
            return new Double[0][0];
        }
        Double[][] inv = new Double[2][2];
        inv[0][0] = mat[1][1] / det;
        inv[0][1] = -mat[0][1] / det;
        inv[1][0] = -mat[1][0] / det;
        inv[1][1] = mat[0][0] / det;
        return inv;
    }
    static double determinant2x2(Double[][] mat) {
        if (mat.length != 2 || mat[0].length != 2) {
            System.out.println("Only 2x2 matrices supported for determinant.");
            return Double.NaN;
        }
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0];
    }

}

/********************************************2-D arrays are used*************************************************/
/* 
static datatype[][] function_name(datatype [][]name,Scanner sacnner_name)
{ _  _ _ - ___ -                -> block of code
  _ _ _  __  _ _ _ 
                    }
  
    Method is declared by static datatype fName(datatype arguments)
*/