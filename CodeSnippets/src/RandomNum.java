/**
 * How much do you like the snippet in a scale from (1(bad) to 5(good)), may leave your comments below
 *
 * Norman: 2
 * Anabell:
 * Jonas
 *
 */

import javax.sound.midi.Soundbank;

public class RandomNum {

    public static void main(String[] args) {
        System.out.println();
        System.out.println("4");
        System.out.println();
        System.out.println("5");
        System.out.println();
        int[] input = {5, 4, 3, 2, 2};
        int result = computeResult(input);
        System.out.println(result);
    }

    public static int computeResult(int[] input) {
        int tempResult = 0;
        int sum = 0;
        for (int value : input) {
            if (value % 2 == 0) {
                tempResult = tempResult + value;
                tempResult = tempResult * value;
            } else {
                tempResult = 0;
                sum = sum + value;
            }
        }

        tempResult = tempResult - sum;

        int result = 0;
        for (int value : input) {
            if (value >= tempResult) {
                result++;
            }
        }

        return result;
    }
}
