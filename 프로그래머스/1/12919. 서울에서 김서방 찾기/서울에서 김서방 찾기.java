class Solution {
    public String solution(String[] seoul) {
        String s1 = "김서방은 ";
        String s2 = "에 있다";
        String kim = "Kim";
        int a = 0;
        for (int i = 0; i < seoul.length; i++) {
            if (seoul[i].equals(kim)) {
                a = i;
            }
        }
        return s1 + a + s2;
    }
}