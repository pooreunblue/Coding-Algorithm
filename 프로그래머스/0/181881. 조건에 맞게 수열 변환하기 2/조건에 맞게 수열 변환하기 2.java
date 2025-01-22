class Solution {
    public int solution(int[] arr) {
        int count = 0;
        boolean isNotSame = true;
        while(isNotSame) {
            count++;
            isNotSame = false;
            for(int i=0; i<arr.length; i++) {
                if(arr[i] >=50 && arr[i] % 2 == 0) {
                    arr[i] = arr[i] / 2;
                    isNotSame = true;
                } else if(arr[i] < 50 && arr[i] % 2 == 1) {
                    arr[i] = arr[i] * 2 + 1;
                    isNotSame = true;
                }
            }
        }
        return count - 1;
    }
}