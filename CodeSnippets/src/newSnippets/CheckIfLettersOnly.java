package newSnippets;

public class CheckIfLettersOnly {

    public static boolean checkIfLettersOnly(String stringToTest) {
        char ch;
        int i = 0;
        while (i < stringToTest.length()) {
            ch = stringToTest.charAt(i);
            if (!(ch >= 'a' && ch <= 'z') && !(ch >= 'A' && ch <= 'Z'))
                return false;
            i++;
        }
        return true;
    }

    public static void main(String[] args) {
        String stringToTest = "HelloWorld123";
        if (checkIfLettersOnly(stringToTest))
            System.out.println("Yes");
        else
            System.out.println("No");
    }

}