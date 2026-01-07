import java.util.*;
public class Main {
    static final int MAX = 100000;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        Queue<Integer> q = new ArrayDeque<>();
        boolean[] visited = new boolean[MAX+1];
        int[] dist = new int[MAX+1];

        q.offer(n);
        visited[n] = true;

        while(!q.isEmpty()){
            int cur = q.poll();
            if (cur == k) break;

            for (int i : new int[]{cur+1, cur -1, cur *2}){
                if (i < 0 || i>MAX) continue;
                if (visited[i]) continue;
                visited[i] = true;
                dist[i] = dist[cur] + 1;
                q.offer(i);
            }
        }
        System.out.println(dist[k]);
    }
}
