import java.util.*;
class Solution {
    public String solution(String s) {
        String answer = "";
        String[] str = s.split(" ");
        List<Integer> in = new ArrayList<>();
        
        for(int i = 0; i < str.length; i++){
           in.add(Integer.parseInt(str[i]));
        }
        answer = Collections.min(in) + " " + Collections.max(in);
        return answer;
    }
}