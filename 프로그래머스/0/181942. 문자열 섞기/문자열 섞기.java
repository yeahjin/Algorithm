class Solution {
    public String solution(String str1, String str2) {
        char[] a = str1.toCharArray();
        char[] b = str2.toCharArray();
        String answer = "";
        for(int i = 0; i < str1.length(); i++){
            answer += a[i];
            answer += b[i];
        }
        return answer;
    }
}