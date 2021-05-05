package extras;

public class isPrime {

    public static void main(String[] args) {
        int number = 11;
        System.out.println(isPrime(11));
    }

    public static boolean isPrime(int number) {
        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}
