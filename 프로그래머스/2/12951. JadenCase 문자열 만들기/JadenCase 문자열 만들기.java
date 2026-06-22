import java.util.*;

class Solution {
    public String solution(String s) {
        boolean isFirst = true;
        StringBuilder sb = new StringBuilder();
        for (String c : s.split("")) {
            sb.append(isFirst ? c.toUpperCase() : c.toLowerCase());
            isFirst = c.equals(" ");
        }
        return sb.toString();
    }
}