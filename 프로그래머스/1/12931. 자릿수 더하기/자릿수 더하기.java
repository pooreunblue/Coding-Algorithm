import java.util.*;

public class Solution {
    public int solution(int n) {
        int result = 0;
        String number = Integer.toString(n);
        String[] numbers = number.split("");
        for (String i: numbers) {
            result += Integer.parseInt(i);
        }
        return result;
    }
}