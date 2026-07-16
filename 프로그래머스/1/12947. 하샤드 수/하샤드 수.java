class Solution {
    public boolean solution(int x) {
        boolean answer = false;
        int sum = 0;
        String num = x + "";
        String[] nums = num.split("");
        for(String n : nums) {
            sum += Integer.parseInt(n);
        }
        if (x % sum == 0) {
            answer = true;
        }
        return answer;
    }
}