class Solution {
    public int[] solution(String my_string) {
        int[] answer = new int[52];
/* 
'A'부터 'Z'까지 개수를 확인하는 26번의 루프를 my_string의 길이만큼 루프, 하나하나 길이 52의 배열에 저장 
*/
        for(int i=0; i<my_string.length(); i++) {
            char c = my_string.charAt(i);
            if('A'<=c&&c<='Z') {
                answer[c-'A']++;
            } else if('a'<=c&&c<='z') {
                answer[26+c-'a']++;
            }
        }
        return answer;
    }
}

