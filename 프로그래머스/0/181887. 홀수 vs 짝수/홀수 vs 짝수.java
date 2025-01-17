class Solution {
    public int solution(int[] num_list) {
        int sumOfOdd = 0;
        int sumOfEven = 0;
        for(int i=0; i < num_list.length; i+=2) {
            sumOfOdd += num_list[i];
        }
        for(int i=1; i < num_list.length; i+=2) {
            sumOfEven += num_list[i];
        }
        if(sumOfOdd == sumOfEven) {
            return sumOfOdd;
        }
        return Math.max(sumOfOdd,sumOfEven);
    }
}