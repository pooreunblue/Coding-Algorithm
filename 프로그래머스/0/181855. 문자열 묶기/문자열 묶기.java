import java.util.Arrays;

class Solution {
    public int solution(String[] strArr) {
        int max = 0;
        for (int i = 0; i < strArr.length; i++) {
            max = Math.max(strArr[i].length(), max);
        }
        int[] num = new int[max + 1];
        for (int i = 0; i < strArr.length; i++) {
            num[strArr[i].length()]++;
        }
        int nMax = 0;
        for (int i = 0; i < num.length; i++) {
            if (nMax < num[i]) {
                nMax = num[i];
            }
        }
        int answer = nMax;
        return answer;
    }
}