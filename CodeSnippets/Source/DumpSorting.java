/**
 * How much do you like the snippet in a scale from (1(bad) to 5(good)), may leave your comments below
 *
 * Anabelle:4
 * Norman: 3
 * Jonas
 *
 */


import java.util.Arrays;
import java.util.List;

class dumpSorting {

    public static void main(String[] args) {
        System.out.println();
        System.out.println("[12, 11, 9, 8]");
        System.out.println();
        System.out.println("[11, 9, 12, 8]");
        System.out.println();
        int a = 9;
        int b = 12;
        int c = 8;
        int d = 11;
        System.out.println(sort(a, b, c, d));
    }

    public static List<Integer> sort(int a, int b, int c, int d) {
        if (a > b) {
            int temp = b;
            b = a;
            c = temp;
        }
        if (c > d) {
            int temp = d;
            d = c;
            c = temp;
        }
        if (a > c) {
            int temp = c;
            c = a;
            a = temp;
        }
        if (b > d) {
            int temp = d;
            d = b;
            b = temp;
        }
        if (b > c) {
            int temp = c;
            c = b;
            b = temp;
        }

        return Arrays.asList(a, b, c, d);
    }

}
