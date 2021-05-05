package totallyNewSnippets;

/**
 * How much do you like the snippet in a scale from (1(bad) to 5(good)), may leave your comments below
 *
 * Norman:
 * Annabelle: 4
 * Jonas
 *
 */

public class NumberOfLeaves {
    public static void main(String[] args) {
        HeightOfTree.Node n = new HeightOfTree.Node();
        n.left = new HeightOfTree.Node();
        n.right = new HeightOfTree.Node();
        n.left.left = new HeightOfTree.Node();
        n.left.left.left = new HeightOfTree.Node();
        n.left.left.right = new HeightOfTree.Node();
        System.out.println(getNumberOfLeaves(n));
    }

    public static class Node {
        HeightOfTree.Node left, right;
        int value;
    }

    public static int getNumberOfLeaves(HeightOfTree.Node n) {
        int numberOfLeaves = 0;
        if (n.left == null && n.right == null)
            numberOfLeaves += 1;
        if (n.left != null) {
            numberOfLeaves += getNumberOfLeaves(n.left);
        }
        if (n.right != null) {
            numberOfLeaves += getNumberOfLeaves(n.right);
        }
        return numberOfLeaves;
    }
}
