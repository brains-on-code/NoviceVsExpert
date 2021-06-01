public class GFG {


    static int min(int x, int y, int z) {
        if (x < y)
            return (x < z) ? x : z;
        else
            return (y < z) ? y : z;
    }

    static int minCost(int cost[][], int m, int n) {
        if (n < 0 || m < 0) {
            return Integer.MAX_VALUE;
        } else if (m == 0 && n == 0) {
            return cost[m][n];
        } else {
            int a = minCost(cost, m - 1, n - 1);
            int b = minCost(cost, m - 1, n);
            int c = minCost(cost, m, n - 1);
            return cost[m][n] + min(a, b, c);
        }
    }

}