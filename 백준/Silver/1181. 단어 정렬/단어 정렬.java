import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        Set<String> s = new HashSet<>();
        for (int i = 0 ; i < n ;i++){
            s.add(sc.next());
        }
        List<String> list = new ArrayList<>(s);
        Collections.sort(list, (a, b) -> {
            if (a.length() == b.length()) return a.compareTo(b);
            return a.length() - b.length();
        });

        for (String str : list){
            System.out.println(str);
        }

    }
}