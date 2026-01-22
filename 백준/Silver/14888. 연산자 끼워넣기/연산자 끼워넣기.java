import java.util.*;
public class Main {
    static int N;
    static int[] list;
    static int a, b, c, d;
    static int MAX = Integer.MIN_VALUE;
    static int MIN = Integer.MAX_VALUE;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        list = new int[N];
        for (int i = 0; i < N; i++) list[i] = sc.nextInt();
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        d = sc.nextInt();
        dfs(1, a,b,c,d,list[0]);
        System.out.println(MAX);
        System.out.println(MIN);
    }
    public static void dfs(int dep, int a, int b, int c, int d, int sum){
        if (dep == N){
            MAX = Math.max(MAX, sum);
            MIN = Math.min(MIN, sum);
            return;
        }
        if (a > 0) dfs(dep + 1, a - 1, b, c, d, sum + list[dep]);
        if (b > 0) dfs(dep + 1, a, b - 1, c, d, sum - list[dep]);
        if (c > 0) dfs(dep + 1, a, b, c - 1, d, sum * list[dep]);
        if (d > 0) dfs(dep + 1, a, b, c, d - 1, sum / list[dep]);
    }

}
