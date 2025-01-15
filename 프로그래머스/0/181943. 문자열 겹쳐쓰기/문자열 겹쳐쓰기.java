import java.util.Scanner;

class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        int len1 = my_string.length();
        int len2 = overwrite_string.length();
        
        String str1 = my_string.substring(0,s) + overwrite_string;
        String str2 = my_string.substring(s+len2);
        answer = str1 + str2;
     return answer;
    }
}