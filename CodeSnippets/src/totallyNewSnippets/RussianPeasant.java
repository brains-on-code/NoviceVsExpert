package totallyNewSnippets;

/**
 * How much do you like the snippet in a scale from (1(bad) to 5(good)), may leave your comments below
 *
 * Annabelle: 2 bitoperations might be unkown
 * Norman: 3 (bit shift is tricky, but would be fine as a test)
 * Jonas
 *
 */

public class RussianPeasant {

    public static void main(String[] args) {
        System.out.println(russianPeasant(18, 3));
    }

    public static int russianPeasant(int a, int b) {
        int res = 0;

        while (b > 0) {
            if ((b & 1) != 0) {
                res = res + a;
            }

            a = a << 1;
            b = b >> 1;
        }
        return res;
    }
}
