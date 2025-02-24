import java.util.*;

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int maxNum = Arrays.stream(array).max().getAsInt();
        int[] numArr = new int[maxNum+1];
        for(int i=0; i<array.length; i++) {
            numArr[array[i]]++;
        }
        int max = numArr[0];
        for(int i=1; i<numArr.length; i++) {
            if(numArr[i] > max) {
                max = numArr[i];
                answer = i;
            } else if(numArr[i] == max) {
                answer = -1;
            }
        }
        return answer;
    }
}