class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        for(int[] query : queries) {
            for(int i=0; i<arr.length; i++) {
                if(i>=query[0] && i<=query[1]){
                    arr[i]++;
                }
            }
        }
        return arr;
    }
}