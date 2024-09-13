class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String as = Integer.toString(a);
        String bs = Integer.toString(b);
        String a2 = as + bs;
        String b2 = bs + as;
        int t1 = Integer.parseInt(a2);
        int t2 = Integer.parseInt(b2);
        if (t1 > t2){
            answer = t1;
        }
        else{
            answer = t2;
        }
        
        
        return answer;
    }
}