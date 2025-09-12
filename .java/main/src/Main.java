
import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws Exception {

        // Устанавливаем кодировку UTF-8 для вывода
    //    System.setOut(new PrintStream(System.out, true, "UTF-8"));
       Scanner input = new Scanner(System.in);

       String name, surName;
       int yearBorn, yearNow;

       System.out.println("Как вас зовут?");
       name = input.nextLine();

       System.out.println("Ваша фамилия?");
       surName = input.nextLine();

       System.out.println("Какой сейчас год?");
       yearNow = input.nextInt();

       System.out.println("В каком году вы родились?");
       yearBorn = input.nextInt();

       System.out.println("Рад познакомиться, " + name + " " + surName + "!");
       System.out.println("Вам сейчас " + (yearNow - yearBorn) + " лет");

    byte a = 1;
    int b = a;

    b = (b*5);
    System.out.println(b);

    }
}