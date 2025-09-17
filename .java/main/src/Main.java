class Example{
    int a;
    boolean b;
    String s;
}



public class Main {
    public static void main(String[] args) {


        int [] a = new int[10];
        for (int x: a){
            System.out.print(x);
        }
        System.out.println();
        int [] b = a.clone();
        b[1] = -3;
        for (int x: b){
            System.out.print(x);
        }

        for (int x: a){
            System.out.print(x);
        }
        System.out.println();


        int [] [] coord = {{1, 2, 3}, {4, 5, 6}};
        for (int []tmp1: coord){
            for (int tmp2: tmp1){
                System.out.print(tmp2 + "\t");
            }
            System.out.print("\n");
        }
        System.out.print("max chmo");    
    }
}