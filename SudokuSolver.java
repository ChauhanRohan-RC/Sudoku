
public class SudokuSolver {
    public static int Void = 0;

    private static boolean check(int[][] board, int[] pos, int num) {
        int row = pos[0]; int col = pos[1];

        // check row
        for (int i=0; i < board[row].length; i++) {
            if (board[row][i] == num && i != col) { return false; }
        }

        // check column
        for (int i=0; i < board.length; i++) {
            if (board[i][col] == num && i != row) { return false; }
        }

        // check box
       int bx = (col / 3) * 3; int by = (row / 3) * 3;
       for (int r = by; r < by + 3; r++) {
           for (int c = bx; c < bx + 3; c++) {
                if (board[r][c] == num && (row != r || col != c)) { return false; }
           }
       }

        return true;
    }

    private static int[] getVoid(int[][] board) {
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {
                if (board[r][c] == Void) { return new int[]{r, c}; }
            }
        }
        return null;
    }

    public static boolean solve(int[][] board) {
        int[] VoidPos = getVoid(board);

        if (VoidPos == null) { return true; }        // If no Void left

        int row = VoidPos[0], col = VoidPos[1];
        for (int i = 1; i < 10; i++) {
            if (check(board, VoidPos, i)) {
                board[row][col] = i;

                if (solve(board)) { return true; }  // Backtracking Recursion

                board[row][col] = Void;             // Resetting void
            }
        }

        return false;
    }

    public static String toString(int[][] board) {
        StringBuilder str = new StringBuilder();
        for(int r = 0; r < board.length; r++) {
            if (r !=0 && r % 3 == 0) {str.append("----------------------\n");}
            for(int c = 0; c < board[0].length; c++) {
                if (c !=0 && c % 3 == 0) { str.append("| "); }
                str.append(board[r][c]).append(' ');
            }
            str.append('\n');
        }

        return str.toString();
    }

    public static void main(String[] args) {

        // Sudoku Board (2D Array)
        int[][] board = new int[][]
                {
                {0, 0, 0, 0, 8, 0, 0, 0, 0},
                {8, 0, 9, 0, 7, 1, 0, 2, 0},
                {4, 0, 3, 5, 0, 0, 0, 0, 1},
                {0, 0, 0, 1, 0, 0, 0, 0, 7},
                {0, 0, 2, 0, 3, 4, 0, 8, 0},
                {7, 3, 0, 0, 0, 9, 0, 0, 4},
                {9, 0, 0, 0, 0, 0, 7, 0, 2},
                {0, 0, 8, 2, 0, 5, 0, 9, 0},
                {1, 0, 0, 0, 4, 0, 3, 0, 0}
                };

        // Solving Sudoku Board
        long startTime = System.nanoTime();
        solve(board);
        double timeTaken = (double) (System.nanoTime() - startTime) / 10E9;

        // Printing Sudoku Board
        System.out.println(toString(board));
        System.out.printf("--> Completed in %.8f seconds\n", timeTaken);
    }
}
