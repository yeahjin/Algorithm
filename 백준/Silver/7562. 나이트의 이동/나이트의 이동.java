import java.util.*;
public class Main {
    static final int[] dx = {-1,-2,-2,-1,1,2,2,1};
    static final int[] dy = {-2,-1,1,2,-2,-1,1,2};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int test_case = sc.nextInt();

        for (int t = 0; t < test_case; t++){
            int l = sc.nextInt();
            int start_x = sc.nextInt();
            int start_y = sc.nextInt();
            int end_x = sc.nextInt();
            int end_y = sc.nextInt();

            int[][] dist = new int[l][l];
            boolean[][] visited = new boolean[l][l];
            Queue<int[]> q = new ArrayDeque<>();
            visited[start_x][start_y] = true;
            dist[start_x][start_y] = 0;
            q.offer(new int[]{start_x, start_y});

            while (!q.isEmpty()){
                int[] cur = q.poll();
                int x = cur[0];
                int y = cur[1];
                if (x == end_x && y == end_y){
                    break;
                }
                for (int i = 0; i < 8; i++){
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if (nx < 0 || nx >= l || ny < 0 || ny >= l) continue;
                    if (visited[nx][ny]) continue;
                    visited[nx][ny] = true;
                    dist[nx][ny] = dist[x][y] + 1;
                    q.offer(new int[] {nx, ny});
                }
            }
            System.out.println(dist[end_x][end_y]);

        }
    }
}
