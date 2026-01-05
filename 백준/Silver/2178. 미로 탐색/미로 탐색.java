import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    final static int[] dx = {0,0,1,-1};
    final static int[] dy = {1,-1,0,0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] grid = new int[n][m];
        int[][] dist = new int[n][m];
        boolean[][] visited = new boolean[n][m];

        for (int i = 0; i < n; i++){
            String line = br.readLine().trim();
            for(int j = 0; j < m; j++){
                grid[i][j] = line.charAt(j) - '0';
            }
        }

        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{0,0});
        dist[0][0] = 1;
        visited[0][0] = true;

        while (!q.isEmpty()){
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];
            for (int dis = 0; dis < 4; dis++){
                int nx = x + dx[dis];
                int ny = y + dy[dis];

                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                if (grid[nx][ny] == 0) continue;
                if (visited[nx][ny]) continue;

                q.offer(new int[] {nx, ny});
                dist[nx][ny] = dist[x][y] + 1;
                visited[nx][ny] = true;
            }
        }

        System.out.println(dist[n-1][m-1]);
    }

}