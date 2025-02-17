class Solution {
    public int solution(String[] order) {
        int answer = 0;
        for(String drink : order) {
            if(drink.contains("americano") || drink.contains("anything")) {
                answer += 4500;
            } else {
                answer += 5000;
            }
        }
        return answer;
    }
}