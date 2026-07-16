class Solution {
    public long solution(long n) {
        double x = Math.sqrt(n);
        int y = 0;
        if (x % 1 == 0) {
            y = (int)x + 1;
        } else {
            return -1;
        }
        return (long) Math.pow(y, 2);
    }
}