import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int max = tangerine[0];
        for (int i = 1; i < tangerine.length; i++) {
            if (tangerine[i] > max) {
                max = tangerine[i];
            }
        }
        int[] array = new int[max+1];
        for (int i=0; i < tangerine.length; i++) {
            array[tangerine[i]] += 1;
        }
        Arrays.sort(array);
        int sum = 0;
        int count = 0;
        for (int i = array.length-1; i >= 0; i--) {
            sum += array[i];
            count += 1;
            if (sum >= k) {
                break;
            }
        }
        return count;
    }
}