import java.util.Arrays;

class Solution {
    public int[] solution(int[] numList) {
        Arrays.sort(numList);
        return Arrays.copyOf(numList, 5);
    }
}