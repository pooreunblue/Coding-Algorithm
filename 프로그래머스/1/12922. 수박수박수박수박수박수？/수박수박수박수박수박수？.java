import java.util.*;

class Solution {
    public String solution(int n) {
        String[] arr = new String[n];
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                arr[i] = "수";
            } else {
                arr[i] = "박";
            }
        }
        return String.join("", arr);
    }
}