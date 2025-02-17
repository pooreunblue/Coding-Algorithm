/*
String[] picture의 모든 String을 ""로 split하면 새로운 String[]에 모든 요소들이 하나씩 들어간다. 모든 요소들에 대해서 repeat(2), join, 그리고
*/
import java.util.*;

class Solution {
    public String[] solution(String[] picture, int k) {
        List<String> answer = new ArrayList<>();
        for(int i=0; i<picture.length; i++) {
            String[] arrStr = picture[i].split("");
            String str = "";
            for(int j=0; j<arrStr.length; j++) {
                str += arrStr[j].repeat(k);
            }
            for(int j=0; j<k; j++) {
                answer.add(str);
            }
        }
        return answer.toArray(new String[answer.size()]);
    }
}