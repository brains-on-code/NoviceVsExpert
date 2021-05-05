package newSnippets;

/**
 * How much do you like the snippet in a scale from (1(bad) to 5(good)), may leave your comments below
 *
 * Norman:
 * Annabelle: 1 too easy
 * Jonas
 *
 */

public class Student {
    private final String name;
    private int age;

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public int getAge() {
        return age;
    }

    public int hadBirthday() {
        return age = age + 1;
    }

    public static void main(String[] args) {
        Student willi = new Student("Willi", 25);
        willi.hadBirthday();
        System.out.print(willi.getAge());
    }
}
