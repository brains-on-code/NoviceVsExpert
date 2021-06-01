public class PrintBench {
    public static void main(String[] args) {
        Random r = new Random();
        for (int i = 0; i < 1000; i++) {
            for (int j = 0; j < 1000; j++) {
                if (r.nextInt(4) == 0) {
                    System.out.print("O");
                } else {
                    System.out.print("#");
                }
            }

            System.out.println("");
        }
    }
}