import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;

public class Main {

    public static void main(String[] args) {


        Scanner scanner = new Scanner(System.in);
        String n = scanner.nextLine();

        while (scanner.hasNextLine()) {

            String lineOfString = scanner.nextLine();

            System.out.println(returnCorrectValue(lineOfString));
        }

    }

    public static String returnCorrectValue(String lineOfString){

        lineOfString = lineOfString.replace( " ", "");

        if (lineOfString.length() % 2 == 0) {
            // create list containing each string character as Character
            List<Character> charList = new ArrayList<>();
            Stack<Character> stack = new Stack<>();
            for (int i = 0; i < lineOfString.length(); i++) {
                charList.add(lineOfString.charAt(i));
            }
            // loop over each element in list and check if between same character appearance there is even gap.
            for (char character : charList) {

                if (character == '(' || character == '[') {
                    stack.push(character);
                } else {
                    if (character == ')') {

                        if (stack.isEmpty()) {
                            return "No";
                        } else if (stack.pop() != '(') {
                            return "No";
                        }

                    } else if (character == ']') {
                        if (stack.isEmpty()) {
                            return "No";
                        } else if (stack.pop() != '[') {
                            return "No";
                        }
                    }
                }
            }
            if (stack.isEmpty()) {
                return "Yes";
            } else {
                return "No";
            }
        }
        return "No";
    }
}
