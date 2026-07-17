import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> numbers = new ArrayList<>();
        for (int num : arr) {
            numbers.add(num);
        }
        int min = Collections.min(numbers);
        numbers.remove(Integer.valueOf(min));
        if (numbers.isEmpty()) {
            numbers.add(-1);
        }
        int[] answer = numbers.stream().mapToInt(i -> i).toArray();
        return answer;
    }
}