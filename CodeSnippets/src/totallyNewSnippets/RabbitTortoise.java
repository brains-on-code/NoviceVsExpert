package totallyNewSnippets;

/**
 * How much do you like the snippet in a scale from (1(bad) to 5(good)), may leave your comments below
 *
 * Norman: 3, this is a cycle detection, right?
 * Anabell:
 * Jonas
 *
 */

public class RabbitTortoise {

    public static void main(String[] args) {
        int[] field = {1, 2, 3, 4, 4};
        System.out.println(rabbitTortoise(field));
    }

    public static int rabbitTortoise(int[] number_field) {
        int tortoise = number_field[0];
        int rabbit = number_field[number_field[0]];

        while (tortoise != rabbit) {
            tortoise = number_field[tortoise];
            rabbit = number_field[number_field[rabbit]];
        }

        rabbit = 0;
        while (tortoise != rabbit) {
            tortoise = number_field[tortoise];
            rabbit = number_field[rabbit];
        }
        return rabbit;
    }
}
