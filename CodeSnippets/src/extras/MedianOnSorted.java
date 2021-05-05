package extras;

/**
 * How much do you like the snippet in a scale from (1(bad) to 5(good)), may leave your comments below
 *
 * Norman:
 * Annabelle: 4
 * Jonas
 *
 */

public class MedianOnSorted {
    public static void main(String[] args) {
        int[] array = {1, 2, 4, 5, 6, 16};

        System.out.println(median(array));
    }

    public static float median(int[] array) {
        float b;
        if (array.length % 2 == 1)
            b = array[array.length / 2];
        else
            b = (array[array.length / 2 - 1] + array[array.length / 2]) / 2f;
        return b;
    }
}
