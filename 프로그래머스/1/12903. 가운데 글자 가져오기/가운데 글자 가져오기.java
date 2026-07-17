class Solution {
    public String solution(String s) {
        int len = s.length();
        System.out.println(len);
        if (len % 2 == 0) {
            return s.substring((len-1)/2, (len-1)/2 + 2);
        } else {
            return s.substring((len-1)/2, (len-1)/2 + 1);
        }
    }
}