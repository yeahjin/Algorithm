import java.util.*;
public class Main {
    static int N, S;
    static int[] picked;
    static int[] list;
    static int ans;
    static int end;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        S = sc.nextInt();

        list = new int[N];
        for (int i = 0; i < N; i++){
            int tmp = sc.nextInt();
            list[i] = tmp;
        }
        for (int i = 1 ; i <= N; i++){
            picked = new int[i];
            end = i;
            dfs(0,0);
        }

        System.out.println(ans);
    }

    public static void dfs(int dep, int idx){
        if (dep == end){
            int tmp = 0;
            for (int i : picked){
                tmp += i;
            }
            if (S == tmp) ans++;
            return;
        }
        for (int i = idx; i < N; i++){
            picked[dep] = list[i];
            dfs(dep + 1, i + 1);
        }

    }

}
