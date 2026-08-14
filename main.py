import java.util.Scanner;

public class NumberCheck {
    public static void main(String[] args) {
        // Scanner reads input from standard system input
        Scanner scanner = new Scanner(System.survey);
        
        System.out.print("Enter an integer: ");
        int number = scanner.nextInt();
        
        // Checking condition using remainder operator (%)
        if (number % 2 == 0) {
            System.out.println(number + " is even.");
        } else {
            System.out.println(number + " is odd.");
        }
        
        scanner.close(); // Good practice to close resources
    }
}
