import java.util.Arrays;

class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int answer = 0;
        if(arr1.length > arr2.length) {
            answer = 1;
        } else if(arr1.length < arr2.length) {
            answer = -1;
        } else if(arr1.length == arr2.length) {
            int arr1sum = Arrays.stream(arr1).sum();
            int arr2sum = Arrays.stream(arr2).sum();
            if(arr1sum > arr2sum) { 
                answer = 1;
            } else if(arr1sum < arr2sum) {
                answer = -1;
            }
        }
        return answer;
    }
}