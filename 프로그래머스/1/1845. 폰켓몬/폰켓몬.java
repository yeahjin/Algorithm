import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int len = nums.length / 2;
        HashSet<Integer> set = new HashSet<>();
        for(int i: nums){
            set.add(i);
        }
        answer = set.size();
        
        if (answer > len){
            answer = len;
        }
        
        return answer;
    }
}