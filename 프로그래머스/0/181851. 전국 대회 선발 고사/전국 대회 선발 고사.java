import java.util.*;

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        HashMap<Integer, Integer> ranking = new HashMap<>();
        for (int i=0; i<rank.length; i++) {
            if(attendance[i]) {
                ranking.put(rank[i], i);
            }
        }
        ArrayList<Integer> keySet = new ArrayList<>(ranking.keySet());
        Collections.sort(keySet);
        int a = ranking.get(keySet.get(0));
        int b = ranking.get(keySet.get(1));
        int c = ranking.get(keySet.get(2));
        return a * 10000 + b * 100 + c;
    }
}