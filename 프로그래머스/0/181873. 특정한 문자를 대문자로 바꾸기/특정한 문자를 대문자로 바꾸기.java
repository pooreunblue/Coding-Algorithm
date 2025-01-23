class Solution {
    public String solution(String myString, String alp) {
        String upperAlp = alp.toUpperCase();
        return myString.replace(alp, upperAlp);
    }
}