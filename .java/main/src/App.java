import java.util.Random;
import java.util.Scanner;


public class App {
    public static void sayHello() {
        System.out.println("Привет, мир!");
        class Foo{
            int x = 0;
            void privet(){

            }
        }

        }
    

    public static int add(int a, int b){
        return a + b;
    }
    
    public static void main(){

        Scanner input = new Scanner(System.in);
        // System.out.println("привет");
        
        String answer = input.nextLine();
        System.out.println(answer);

        Random rnd = new Random(System.currentTimeMillis());

        // while
        // int a = 10;
        // while (a < 10){
        //     System.out.println(a);
        //     a ++;
        // }
        // System.out.println("cycle done, a = " + a);
        // a = 10;
        // // do while
        // do{
        //     System.out.println(a);
        //     a ++;
        // } while(a < 10);
        // System.out.println("cycle done, a = " + a);

        // // for
        // for (int i = 0; i < 10; i += 2){
        //     System.out.println(i);
        // }

        // System.out.println(rnd.nextInt(100));

        // for(int i = 0; i <= 100; i ++){
        //     if (i == (i/2)*2)
        //         continue;
        //     else
        //         System.out.println("i is odd, i = "  + i);
        // }



        sayHello();
        System.out.println(add(5, 3));
    }
}
