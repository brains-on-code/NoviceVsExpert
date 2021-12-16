
/**
 * How much do you like the snippet in a scale from (1(bad) to 5(good)), may leave your comments below
 *
 * Annabelle:5
 * Norman: 4 (need to discuss identifiers)
 * Jonas
 *
 */

class smallGauss {

    public static void main(String[] args) {
        System.out.println(sum(10));
    }

    public static int sum(int n) {
        int res = 0;
        for (int i = 1; i < n; i++) {
            res += i;
        }
        return res;
    }
}
