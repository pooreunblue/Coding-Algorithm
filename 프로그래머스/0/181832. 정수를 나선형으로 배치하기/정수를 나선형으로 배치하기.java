class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int rowSeq = 0;
        int columnSeq = 0;
        int value = 1;
        int direction = 0;
        while(value <= n*n) {
            answer[rowSeq][columnSeq] = value++;
            if(direction == 0) {
                if(columnSeq < n-1 && answer[rowSeq][columnSeq+1] == 0) {
                    columnSeq++;
                } else {
                    direction = 1;
                    rowSeq++;
                }
            } else if(direction == 1) {
                if(rowSeq < n-1 && answer[rowSeq+1][columnSeq] == 0) {
                    rowSeq++;
                } else {
                    direction = 2;
                    columnSeq--;
                }
            } else if(direction == 2) {
                if(columnSeq > 0 && answer[rowSeq][columnSeq-1] == 0) {
                    columnSeq--;
                } else {
                    direction = 3;
                    rowSeq--;
                }
            } else if(direction == 3) {
                if(rowSeq > 0 && answer[rowSeq-1][columnSeq] == 0) {
                    rowSeq--;
                } else {
                    direction = 0;
                    columnSeq++;
                }
            }
        }
        return answer;
    }
}