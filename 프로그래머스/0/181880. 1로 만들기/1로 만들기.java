import java.util.Arrays;

class Solution {
    public int solution(int[] numList) {
        int[] arr = new int[numList.length];
        int count = 0;
        for(int i=0; i<arr.length; i++) {
            arr[i] = 1;
        }
        while(true) {
            for(int i=0; i<numList.length; i++) {
                if(numList[i] != 1) {
                    numList[i] /= 2;
                    count++;
                }
            }
            if(Arrays.equals(arr, numList)) {
                return count;
            }
        }
    }
}