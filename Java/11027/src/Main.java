import java.util.Scanner;

public class Main {


    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNextInt()) {

            int n = scanner.nextInt();

            System.out.println(returnOnesCount(n));
        }

    }

    public static String returnOnesCount(int n){

        int numberOfOnes = 1;
        int oneCount = 1;

        while (numberOfOnes % n != 0) {
            numberOfOnes = numberOfOnes * 10 + 1;

            numberOfOnes = numberOfOnes % n;
            oneCount++;
        }

        return Integer.toString(oneCount);
    }
}
