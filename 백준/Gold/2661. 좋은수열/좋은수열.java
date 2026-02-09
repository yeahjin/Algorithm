import java.util.*;
public class Main {
    static int N;
    static int[] picked;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        picked = new int[N];
        dfs(0);
    }

    public static void dfs(int dep){
        if (!isGood(dep)){
            return;
        }
        if (dep == N){
            for(int i : picked){
                System.out.print(i);
            }
            System.exit(0);
        }
        for (int i = 1; i <= 3; i++){
            picked[dep] = i;
            dfs(dep + 1);
        }
    }
    public static boolean isGood(int dep){
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < dep; i++) sb.append(picked[i]);

        for (int start = 0 ; start < dep ; start++){
            for (int k = 1; k <= (dep - start)/2 ;k++){
                String a = sb.substring(start, start + k);
                String b = sb.substring(start + k, start + 2 * k);
                if (a.equals(b)){
                    return false;
                }
            }
        }
        return true;
    }
}
