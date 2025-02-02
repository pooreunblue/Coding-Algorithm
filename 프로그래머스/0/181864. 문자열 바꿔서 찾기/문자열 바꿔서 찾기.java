class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        String Atob = myString.replace("A","b");
        String Btoa = Atob.replace("B","a");
        String Upper = Btoa.toUpperCase();
        if(Upper.contains(pat)) {
            return 1;
        }
        return answer;
    }
}