
/**
 * How much do you like the snippet in a scale from (1(bad) to 5(good)), may leave your comments below
 *
 * Annabelle: 4
 * Norman: 4
 * Jonas
 *
 */

class isPrime {

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
