class Solution {
    public int solution(String[] strArr) {
        int answer = 0;
        int max = 0;
        for (int i=0; i < strArr.length; i++) {
            max = Math.max(strArr[i].length(), max);
        }
        int[] arrLength = new int[max + 1];
        for (int i=0; i < strArr.length; i++) {
            arrLength[strArr[i].length()]++;
        }
        for (int i=0; i < arrLength.length; i++) {
            answer = Math.max(arrLength[i], answer);
        }
        return answer;
    }
}