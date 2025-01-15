import java.util.*;
class Solution {
    public int[] solution(int l, int r) {
        List<Integer> list = new ArrayList<>();
        
        for(int i=l; i<=r; i++) {
            String k = i + "";
            int count = 0;
            for(int j=0; j<k.length(); j++){
                if(k.charAt(j)=='0' || k.charAt(j)=='5'){
                count++;
                }
            }
            if(count==k.length()) {
                list.add(i);
            }
        }
        int[] answer = list.stream().mapToInt(i->i).toArray();
        int[] empty = {-1};
        if(answer.length == 0) 
            return empty;
        return answer;
    }
}