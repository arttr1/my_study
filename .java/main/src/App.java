import java.util.Scanner;

public class App {
    static final int NUMBER = 100;
    static final float PI = 3.1415F;



    public static void main(String[] args) {
        System.out.println("Hello, World!");
        System.out.println(NUMBER);
        System.out.println(PI);
        System.out.println("Pi = " + PI);
        
        String S = "nathuA";
        System.out.println(S);   
        
        Scanner scan = new Scanner (System.in);

        String message;
        message = scan.nextLine();

        System.out.println(message);
    }
}
