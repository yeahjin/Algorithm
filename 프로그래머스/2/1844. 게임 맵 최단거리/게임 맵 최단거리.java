import java.util.*;
class Solution {
    static final int[] dx = {0,0,-1,1};
    static final int[] dy = {-1,1,0,0};
    public int solution(int[][] maps) {
        int answer = 0;
        
        int n = maps.length;
        int m = maps[0].length;
        
        Queue<int[]> q = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][m];
        int[][] dist = new int[n][m];
        visited[0][0] = true;
        dist[0][0] = 1;
        q.offer(new int[] {0,0});
        
        while (!q.isEmpty()){
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];
            for (int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 || nx >= n || ny < 0 || ny >=m) continue;
                if (visited[nx][ny]) continue;
                if (maps[nx][ny] == 0) continue;
                visited[nx][ny] = true;
                dist[nx][ny] = dist[x][y] + 1;
                q.offer(new int[] {nx, ny});
            }
        }
        
        return dist[n-1][m-1] == 0 ? -1 : dist[n-1][m-1];
    }
}