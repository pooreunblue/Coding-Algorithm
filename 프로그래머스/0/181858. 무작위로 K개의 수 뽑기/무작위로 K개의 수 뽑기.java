import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, int k) {
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i=0; i < arr.length; i++) {
            if(!answer.contains(arr[i])) {
                answer.add(arr[i]);
            }
            if(answer.size() == k) {
                break;
            }
        }
        if(answer.size() < k) {
            for(int i = answer.size(); i < k; i++) {
                answer.add(-1);
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}