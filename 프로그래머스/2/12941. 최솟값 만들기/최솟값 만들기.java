import java.util.*;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;

        List<Integer> a = new ArrayList<>();
        for(int i= 0; i < A.length; i++){
            a.add(A[i]);
        }
         List<Integer> b = new ArrayList<>();
        for(int i = 0 ; i < B.length; i++){
            b.add(B[i]);
        }
        
        Collections.sort(a);
        Collections.sort(b, Collections.reverseOrder());
        
        for(int i = 0 ; i < A.length; i++){
            answer += a.get(i) * b.get(i);
        }

        return answer;
    }
}