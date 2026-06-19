class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int maxW = 0;
        int maxH = 0;
        for (int[] size: sizes) {
            int w = size[0];
            int h = size[1];
            int max = Math.max(w, h);
            int min = Math.min(w, h);
            maxW = Math.max(max, maxW);
            maxH = Math.max(min, maxH);
            answer = maxW * maxH;
        }
        return answer;
    }
}