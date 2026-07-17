import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int number : arr) {
            list.add(number);
        }
        int min = Collections.min(list);
        list.remove(Integer.valueOf(min));
        if (list.isEmpty()) {
            list.add(-1);
        }
        return list.stream().mapToInt(i -> i).toArray();
    }
}