package totallyNewSnippets;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * How much do you like the snippet in a scale from (1(bad) to 5(good)), may leave your comments below
 *
 * Annabelle: 5
 * Norman: 2 (I like permutation, but isn't there a simpler algorithm? I feel like this one has a lot of syntax, but maybe that's just Java..)
 * Jonas
 *
 */

public class PermuteString {
    public static void main(String[] args) {
        String str = "ABC";
        int n = str.length();
        List<String> result = permute(str, 0, 2);
        for (String permutation : result) {
            System.out.println(permutation);
        }
    }

    public static List<String> permute(String str, int l, int r) {
        List<String> result = new ArrayList<>();
        if (l == r)
            result.add(str);
        else {
            for (int i = l; i <= r; i++) {
                str = swap(str, l, i);
                List<String> temp = permute(str, l + 1, r);
                result.addAll(temp);
                str = swap(str, l, i);
            }
        }
        return result;
    }

    public static String swap(String a, int i, int j) {
        char temp;
        char[] charArray = a.toCharArray();
        temp = charArray[i];
        charArray[i] = charArray[j];
        charArray[j] = temp;
        return String.valueOf(charArray);
    }
}
