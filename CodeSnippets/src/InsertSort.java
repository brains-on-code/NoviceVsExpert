/**
 * How much do you like the snippet in a scale from (1(bad) to 5(good)), may leave your comments below
 *
 * Anabelle: 5
 * Norman: 4
 * Jonas
 *
 */

public class InsertSort {

    public static void main(String[] args) {
        System.out.println();
        System.out.println("7 5 4 3");
        System.out.println();
        System.out.println("5 4 7 3");
        System.out.println();
        int[] unsorted = {3, 7, 4, 5};
        int[] result = sort(unsorted);
        for (int j : result) {
            System.out.print("" + j + " ");
        }
    }

    public static int[] sort(int[] unsorted) {
        for (int i = 1; i < unsorted.length; i++) {
            for (int j = i; j > 0; j--) {
                int jthElement = unsorted[j];
                int jMinusOneElement = unsorted[j - 1];
                if (jthElement < jMinusOneElement) {
                    unsorted[j - 1] = jthElement;
                    unsorted[j] = jMinusOneElement;
                } else {
                    break;
                }
            }
        }
        return unsorted;
    }

}
