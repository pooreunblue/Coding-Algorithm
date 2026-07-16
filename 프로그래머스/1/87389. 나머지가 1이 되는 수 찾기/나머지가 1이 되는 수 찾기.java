class Solution {
    public int solution(int n) {
        int result = 0;
        for(int i = n - 1; i > 0; i--) {
            if (n % i == 1) {
                result = i;
            }
        }
        return result;
    }
}