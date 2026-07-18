class Solution {
    int answer = 0;
    
    public int solution(int[] number) {
        dfs(number, 0, 0, 0);
        return answer;
    }
    
    void dfs(int[] number, int depth, int start, int sum) {
        if (depth == 3) {
            if (sum == 0) {
                answer++;
            }
            return;
        }
        for (int i = start; i < number.length; i++) {
            dfs(number, depth + 1, i + 1, sum + number[i]);
        }
    }
}