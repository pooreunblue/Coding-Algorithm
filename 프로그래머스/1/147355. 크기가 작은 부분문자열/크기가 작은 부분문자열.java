import java.math.*;

class Solution {
    public int solution(String t, String p) {
        int count = 0;
        BigInteger p1 = new BigInteger(p);
        for (int i = 0; i <= (t.length() - p.length()); i++) {
            String s = t.substring(i, i + p.length());
            BigInteger s1 = new BigInteger(s);
            int comparing = s1.compareTo(p1);
            if (comparing > 0) {
                continue;
            }
            count++;
        }
        return count;
    }
}