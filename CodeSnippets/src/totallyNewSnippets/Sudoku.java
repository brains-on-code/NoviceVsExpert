package totallyNewSnippets;

import java.util.List;

public class Sudoku {

    public static void main(String[] args) {
        int[][] field = {
                {1, 0, 0},
                {0, 0, 1},
                {3, 0, 0}
        };

        if (solveEasySudoku(field, 0, 0)) {
            for (int[] row : field) {
                for (int element : row) {
                    System.out.print("" + element + " ");
                }
                System.out.println();
            }
        } else {
            System.out.println("Keine Lösung");
        }
    }

    public static boolean solveEasySudoku(int[][] field, int row, int col) {
        int N = field.length;
        if (row == N - 1 && col == N) {
            return true;
        }
        if (col == N) {
            col = 0;
            row += 1;
        }
        if (field[row][col] != 0) {
            return solveEasySudoku(field, row, col + 1);
        }
        for (int num = 1; num <= N; num++) {
            field[row][col] = num;
            if (!hasProblems(field, row, col)) {
                if (solveEasySudoku(field, row, col)) {
                    return true;
                }
            }
            field[row][col] = 0;
        }
        return false;
    }

    public static boolean hasProblems(int[][] field, int row, int col) {
        for (int i = 0; i < field.length; i++) {
            if (i != col) {
                if (field[row][col] == field[row][i]) {
                    return true;
                }
            }
            if (i != row) {
                if (field[row][col] == field[i][col]) {
                    return true;
                }
            }
        }
        return false;
    }
}
