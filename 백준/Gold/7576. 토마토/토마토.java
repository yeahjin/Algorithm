import java.io.*;
import java.util.*;

public class Main {
    static final int[] dx = {0,0,1,-1};
    static final int[] dy = {1,-1,0,0};
    static int n, m, cntForCompare;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        int[][] grid = new int[n][m];
        int[][] dist = new int[n][m];
        boolean[][] visited = new boolean[n][m];
        Queue<int[]> q = new ArrayDeque<>();

        for (int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++){
                int num = Integer.parseInt(st.nextToken());
                grid[i][j] = num;
                dist[i][j] = 1000000;

                if (num == 1){
                    q.offer(new int[]{i,j});
                    visited[i][j] = true;
                    dist[i][j] = 0;
                } else if (num == -1) {
                    cntForCompare++;
                }
            }
        }

        while(!q.isEmpty()){
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];

            for (int i = 0 ; i < 4; i++){
                int nx = dx[i] + x;
                int ny = dy[i] + y;

                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                if (visited[nx][ny]) continue;
                if (grid[nx][ny] == -1 || grid[nx][ny] == 1) continue;

                q.offer(new int[] {nx, ny});
                dist[nx][ny] = dist[x][y] + 1;
                visited[nx][ny] = true;
            }
        }

        int ans = 0;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (dist[i][j] == 1000000) continue;
                ans = Math.max(ans, dist[i][j]);
            }
        }

        if (!compare(dist)){
            System.out.println(-1);
            return;
        }
        System.out.println(ans);
    }

    public static boolean compare(int[][] grid){
        int cnt = 0;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (grid[i][j] == 1000000) {
                    cnt++;
                }
            }
        }
        return cnt == cntForCompare;
    }
}
