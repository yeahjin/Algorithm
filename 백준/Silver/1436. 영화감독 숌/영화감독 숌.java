import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int cnt = 0;
        for (int i = 666; i < Integer.MAX_VALUE; i++){
            String str = String.valueOf(i);
            if (str.contains("666")){
                cnt++;
            }
            if (cnt == n){
                System.out.println(i);
                break;
            }
        }
    }

}
