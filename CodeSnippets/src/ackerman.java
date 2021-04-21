public class ackerman {

    public static void main(String[] args) {
        int x = 1;
        int y = 1;
        System.out.println("");
        System.out.println(5);
        System.out.println("");
        System.out.println(6);
        System.out.println("");
        System.out.println(ackermann(x, y));
    }

    public static int ackermann(int n, int m) {
        if (n == 0) {
            return m + 1;
        } else if (m == 0) {
            return ackermann(n - 1, 1);
        }

        return ackermann(n - 1, ackermann(n, m - 1));
    }

}
