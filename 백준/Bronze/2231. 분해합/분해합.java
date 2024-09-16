import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int ans = 0;
        for(int i = 1; i <= n; i++) {
            String a = Integer.toString(i);
            int tmp = i;
            for(char c : a.toCharArray()) {
                tmp += Integer.parseInt(String.valueOf(c));
            }
            if (tmp == n){
                ans = i;
                break;
            }
        }
        System.out.println(ans);

    }
}