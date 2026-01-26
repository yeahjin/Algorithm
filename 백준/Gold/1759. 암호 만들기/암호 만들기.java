import java.util.*;

public class Main {
    static int L, C;
    static char[] list;
    static char[] picked;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        L = sc.nextInt();
        C = sc.nextInt();
        list = new char[C];
        picked = new char[L];
        for (int i = 0; i < C; i++) list[i] = sc.next().charAt(0);

        Arrays.sort(list);
        combinations(0,0);

    }
    public static void combinations(int dep, int start){
        if (dep == L){
            int vowel = 0;
            int constant = 0;
            for (int i = 0; i < L; i++){
                if (picked[i] == 'a' || picked[i] == 'e' || picked[i] == 'i' || picked[i] == 'o' || picked[i] == 'u'){
                    vowel++;
                } else{
                    constant++;
                }
            }

            if (vowel >= 1 && constant >= 2){
                for (int i = 0; i < L; i++){
                    System.out.print(picked[i]);
                }
                System.out.println();
            }
            return;
        }
        for (int i = start; i < C; i++){
            picked[dep] = list[i];
            combinations(dep + 1, i + 1);
        }
    }

}
