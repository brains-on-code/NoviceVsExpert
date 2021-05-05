package extras;

public class smallGauss {

    public static void main(String[] args) {
        System.out.println(sum(10));
    }

    public static int sum(int n){
        int res = 0;
        for(int i=1; i<n; i++){
            res += i;
        }
        return res;
    }
}
