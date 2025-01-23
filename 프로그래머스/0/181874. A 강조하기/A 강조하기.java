class Solution {
    public String solution(String myString) {
        String[] arr = myString.split("");
        for(int i=0; i<arr.length; i++) {
            if(arr[i].equals("a")) {
                arr[i] = arr[i].toUpperCase();
            } else if(arr[i].equals("A")) {
                arr[i] = arr[i];                
            } else {
                arr[i] = arr[i].toLowerCase();
            }
        }
        return String.join("", arr);
    }
}