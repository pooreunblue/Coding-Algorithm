class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        for(int i=0; i<myString.length(); i++) {
            String newString = myString.substring(i);
            if(newString.startsWith(pat)) {
                answer++;
            }
        }
        return answer;
    }
}