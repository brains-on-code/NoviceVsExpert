package extras;

public class Palindrome {
    public static void main(String[] args) {
        System.out.println(isPalindrome("otto"));
    }

    public static boolean isPalindrome(String text){
        for(int i=0; i<text.length()/2 -1 ; i++){
            if(text.charAt(i)!=text.charAt(text.length()-1-i)){
                return false;
            }
        }
        return true;
    }

}
