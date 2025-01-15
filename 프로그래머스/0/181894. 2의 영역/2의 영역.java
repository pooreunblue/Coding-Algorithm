import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr) {
        boolean valueExist = false;
        ArrayList<Integer> list = new ArrayList<>();
        for(int i=0; i<arr.length; i++) {
            if(arr[i]==2) {
                valueExist = true;
                list.add(i);
            }
        }
        if(valueExist == true) {
            int min = list.get(0);
            int max = list.get(list.size()-1);
            return Arrays.copyOfRange(arr, min, max+1);
        } else {
            return new int[] {-1};
        }
    }
}