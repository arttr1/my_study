import java.io.PrintStream;
import java.io.UnsupportedEncodingException;

public class App {
    public static void main(String[] args) throws UnsupportedEncodingException{
       PrintStream printStream = new PrintStream(System.out, true, "cp866");
        
       printStream.println("привет");


    }
}
