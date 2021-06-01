class ClosestPair {

    void printClosest(int ar1[], int ar2[], int m, int n, int x) {
        int diff = Integer.MAX_VALUE;
        int res_l = 0, res_r = 0;
        int l = 0, r = n - 1;
        while (l < m && r >= 0) {
            if (Math.abs(ar1[l] + ar2[r] - x) < diff) {
                res_l = l;
                res_r = r;
                diff = Math.abs(ar1[l] + ar2[r] - x);
            }
            if (ar1[l] + ar2[r] > x)
                r--;
            else
                l++;
        }

        System.out.print("The closest pair is [" + ar1[res_l] + ", " + ar2[res_r] + "]");
    }

}