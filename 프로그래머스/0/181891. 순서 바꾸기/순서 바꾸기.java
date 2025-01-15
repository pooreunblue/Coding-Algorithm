import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] list1 = Arrays.copyOfRange(num_list, 0, n);
        int[] list2 = Arrays.copyOfRange(num_list, n, num_list.length);
        int[] list3 = new int[num_list.length];
        System.arraycopy(list2,0,list3,0,list2.length);
        System.arraycopy(list1,0,list3,list2.length,list1.length);
        return list3;
    }
}