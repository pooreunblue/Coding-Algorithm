class Solution {
    public int solution(String myString, String target) {
        int answer = 0;
        if(myString.contains(target)) {
            answer = 1;
        }
        return answer;
    }
}