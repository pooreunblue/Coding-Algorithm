class Solution {
    public int solution(int[] numList, int n) {
        int answer = 0;
        for(int number : numList) {
            if(number == n) answer = 1;
        }
        return answer;
    }
}