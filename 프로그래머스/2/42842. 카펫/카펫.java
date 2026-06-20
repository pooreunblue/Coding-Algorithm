class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int total = brown + yellow;
        for (int i = total; i > 0; i--) {
            int m = total % i;
            int q = total / i;
            if (m == 0 && (i-2) * (q-2) == yellow) {
                answer[0] = i;
                answer[1] = q;
                break;
            }
        }
        return answer;
    }
}