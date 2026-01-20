import java.util.*;
public class Main {
    static int[] picked;
    static int k;
    static int[] list;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true){
            k = sc.nextInt();
            if (k == 0) break;
            list = new int[k];
            picked = new int[6];
            for (int i = 0; i < k; i++) list[i] = sc.nextInt();
            dfs(0,0);
            System.out.println();
        }
    }

    public static void dfs(int dep, int start){
        if (dep == 6){
            for (int i: picked){
                System.out.print(i + " ");
            }
            System.out.println();
            return;
        }
        for (int i = start ; i < k; i++){
            picked[dep] = list[i];
            dfs(dep+1, i +1);
        }
    }

}
