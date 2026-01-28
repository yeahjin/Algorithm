import java.util.*;
public class Main {
    static boolean[][] visited; // 퀸의 위치
    static int N;
    static int cnt;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        visited = new boolean[N][N];
        dfs(0);
        System.out.println(cnt);
    }

    public static void dfs(int row) {
        if (row == N) {
            cnt++;
            return;
        }
        for (int col = 0 ; col < N; col++){
                if (!isSafe(row, col)) continue;
                visited[row][col] = true;
                dfs(row+1);
                visited[row][col] = false;
        }
    }
    public static boolean isSafe(int row, int col){
        for (int i = 0; i < row; i++){
            if (visited[i][col]) return false;
        }
        // \ 대각선
        int r = row - 1;
        int c = col - 1;
        while (r >= 0 && c >= 0){
            if (visited[r][c]) return false;
            r--;
            c--;
        }

        r = row - 1;
        c = col + 1;
        while (r >= 0 && c < N){
            if (visited[r][c]) return false;
            r--;
            c++;
        }
        return true;
    }
}
