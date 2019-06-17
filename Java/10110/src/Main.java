import java.util.Scanner;

public class Main {


    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        double n = -1;
        while ((n = scanner.nextDouble()) != 0) {

            double squareRootN = Math.sqrt(n);

            if (Math.floor(squareRootN) != squareRootN) {
                System.out.println("no");
            } else {
                System.out.println("yes");
            }
        }

    }
}
