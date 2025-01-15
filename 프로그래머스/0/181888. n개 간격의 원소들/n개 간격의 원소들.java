import java.util.List;
import java.util.ArrayList;

class Solution {
    public List<Integer> solution(int[] numList, int n) {
        List<Integer> list = new ArrayList<>();
        for(int i=0; i < numList.length; i+=n) {
            list.add(numList[i]);
        }
        return list;
    }
}