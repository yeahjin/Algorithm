class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        int t1 = Integer.parseInt((Integer.toString(a) + Integer.toString(b)));
        int t2 = 2 * a * b;
        
        return Math.max(t1,t2);
    }
}