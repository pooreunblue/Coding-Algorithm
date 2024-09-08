class Solution {
    public int solution(String my_string, String is_suffix) {
        String[] my_suf = new String[my_string.length()];
        int answer = 0;
        for(int i=0; i<my_string.length(); i++) {
            my_suf[i] = my_string.substring(i);
            for(String j : my_suf) {
                if(is_suffix.equals(j)) {
                    answer = 1;
                }
            }
        }
        return answer;
    }
}