import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class Main {
    static List<Integer> computer_network;

    private static void createComputerList(int computer_count) {
        computer_network = new ArrayList<>();
        for (int i = 0; i < computer_count; i++) {
            computer_network.add(i);
        }
    }

    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        StringBuilder out = new StringBuilder();

        int cases = Integer.parseInt(scanner.nextLine());
        int successful, unSuccessful;
        String line;
        String [] line_spitted;

        scanner.nextLine(); // skip empty line
        for (int i = 0; i < cases; i++){
            successful = 0;
            unSuccessful = 0;
            createComputerList(Integer.parseInt(scanner.nextLine()));
            while((line = scanner.nextLine()) != null && !line.equals("")){
                line_spitted = line.split(" ");
                if(line_spitted[0].charAt(0) == 'c'){
                    connectComputeres(Integer.parseInt(line_spitted[1])-1,Integer.parseInt(line_spitted[2])-1);
                }else{
                    if(isConnected(Integer.parseInt(line_spitted[1])-1,Integer.parseInt(line_spitted[2])-1))
                        successful++;
                    else
                        unSuccessful++;
                }
                for (Integer i_ : computer_network) {
                    System.out.println(i_);
                }
                System.out.println();
            }
            out.append(successful + "," + unSuccessful + "\n");
            if(i != cases-1)
                out.append("\n");

        }
        System.out.print(out);
    }

    static int connect(int i){
        if (computer_network.get(i) == i) {
            return i;
        } else {
            return (computer_network.set(i, connect(computer_network.get(i))));
        }
    }

    static void connectComputeres(int i, int j){
        computer_network.set(connect(i), connect(j));
    }
    static boolean isConnected(int i, int j){
        return connect(i) == connect(j);
    }
}


