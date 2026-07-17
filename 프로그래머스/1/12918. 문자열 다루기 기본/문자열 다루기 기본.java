import java.util.*;

class Solution {
    public boolean solution(String s) {
        char[] arr = s.toCharArray();
        if (s.length() == 4 || s.length() == 6) {
            for (char c : arr) {
                if (!Character.isDigit(c)) {
                    return false;
                }
            } 
        } else {return false;}
        return true;
    }
}