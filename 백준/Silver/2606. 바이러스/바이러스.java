import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int computer = sc.nextInt();
        boolean[] visited = new boolean[computer+1];
        int node = sc.nextInt();

        Queue<Integer> q = new ArrayDeque<>();
        HashMap<Integer,ArrayList<Integer>> hm = new HashMap<>();
        for (int i =0 ; i < computer; i++){
            hm.put(i+1, new ArrayList<>());
        }

        for (int i = 0; i < node ; i++){
            int key = sc.nextInt();
            int value = sc.nextInt();
            hm.get(key).add(value);
            hm.get(value).add(key);
        }

        q.offer(1);
        visited[1] = true;
        int cnt = 0;

        while (!q.isEmpty()){
            int cur = q.poll();
            cnt++;
            for (int i : hm.get(cur)){
                if (visited[i]) continue;
                visited[i] = true;
                q.offer(i);
            }
        }
        System.out.println(cnt -1);
    }

}
