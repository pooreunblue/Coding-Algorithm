class Solution {
    public int solution(String numStr) {
        int answer = 0;
        String[] numArr = numStr.split("");
        for(int i=0; i<numArr.length; i++) {
            answer += Integer.parseInt(numArr[i]);
        }
        return answer;
    }
}