class Solution {
    public int solution(int[] numList) {
        int answer = 1;
        int length = numList.length;
        for(int i=0; i<length; i++) {
            if(length>10) {
                answer += numList[i];
            } else{
                answer *= numList[i];
            }
        }
        if(length>10) {
            answer = answer - 1;
        }
        return answer;
    }
}