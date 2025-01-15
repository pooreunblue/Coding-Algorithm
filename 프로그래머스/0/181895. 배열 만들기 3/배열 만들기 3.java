import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int[] arr, int[][] intervals) {
        ArrayList<Integer> list = new ArrayList<>();
        for(int[] interval : intervals) {
            for(int i=interval[0]; i<=interval[1]; i++) {
              list.add(arr[i]);
            }
        }
        return list;
    }
}