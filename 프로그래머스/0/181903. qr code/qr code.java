class Solution {
    public String solution(int q, int r, String code) {
        String answer = "";
        char[] arr = code.toCharArray();
        for(int i=0; i<arr.length; i++) {
                answer += i % q == r ? arr[i] : "";
        }
        return answer;
    }
}