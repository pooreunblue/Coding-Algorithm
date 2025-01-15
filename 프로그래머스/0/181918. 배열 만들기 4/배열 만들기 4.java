import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> list = new ArrayList<>();

        for (int i=0; i < arr.length;) {
            if (list.size() == 0) {
                list.add(arr[i]);
                i++;
            } else {
                if (list.get(list.size() - 1) < arr[i]) {
                    list.add(arr[i]);
                    i++;
                } else {
                    list.remove(list.size() - 1);
                }
            }
        }

        int[] stk = list.stream().mapToInt(j -> j).toArray();

        return stk;
    }
}
