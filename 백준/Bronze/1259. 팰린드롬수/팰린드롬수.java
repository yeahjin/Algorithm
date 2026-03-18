import java.util.*;
public class Main
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true){
            String num = sc.next();
            if (num.equals("0")) break;
            if (reversStr(num).equals(num)){
                System.out.println("yes");
            }else{
                System.out.println("no");
            }
        }
    }

    public static String reversStr(String str){
        StringBuilder sb = new StringBuilder();
        for (int i = str.length()-1; i >= 0; i--){
            sb.append(str.charAt(i));
        }
        return sb.toString();
    }

}