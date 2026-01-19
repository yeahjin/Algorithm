import java.util.*;
public class Main {
    static int N, S;
    static int[] list;
    static int ans;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        S = sc.nextInt();

        list = new int[N];
        for (int i = 0; i < N; i++){
            list[i] = sc.nextInt();
        }

        dfs(0,0);

        if (S == 0) ans--;

        System.out.println(ans);
    }

    public static void dfs(int dep, int num){
        if (dep == N){
            if (num == S) ans++;
            return;
        }
        dfs(dep+1, num + list[dep]); // 선택함
        dfs(dep+1, num); // 선택 안함
    }

}
