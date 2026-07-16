import java.util.*;

class Solution {
    public long solution(long n) {
        List<Integer> list = new ArrayList<>();
        String number = n + "";
        System.out.println(number);
        String[] numbers = number.split("");
        Arrays.sort(numbers, Collections.reverseOrder());
        String result = String.join("", numbers);
        return Long.parseLong(result);
    }
}