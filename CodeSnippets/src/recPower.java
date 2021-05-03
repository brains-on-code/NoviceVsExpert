public class recPower {

    public static void main(String[] args) {
        System.out.println();
        System.out.println("64");
        System.out.println();
        System.out.println("243");
        System.out.println();
        System.out.println(power(3, 4));
    }

    public static int power(int base, int exponent) {
        if (exponent == 0) {
            return 1;
        }

        if (exponent == 1) {
            return base;
        }

        return base * power(base, exponent - 1);
    }

}