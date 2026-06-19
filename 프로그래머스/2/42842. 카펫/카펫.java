class Solution {
    public int[] solution(int brown, int yellow) {
        System.out.println("brown = " + brown);
        System.out.println("yellow = " + yellow);

        int[] answer = new int[2];
        int total = brown + yellow;
        int w = 0;
        int h = 0;
        for (int i = total; i >= 1; i--) {
            w = i;
            if (total % i == 0) {
                h = total / w;
                if ((w-2) * (h-2) == yellow) {
                    answer[0] = w;
                    answer[1] = h;
                    break;
                }
            }
        }
        return answer;
    }
}