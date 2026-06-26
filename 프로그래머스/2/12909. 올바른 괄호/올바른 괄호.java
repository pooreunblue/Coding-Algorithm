/**
* 이전에 파이썬으로 풀어보았던 문제인지라 자바로 다시 처음부터 풀이하였습니다.
* 1. ArrayDeque로 스택 구현
* 2. 문자열 s를 문자 배열로 변환시켜 하나씩 순회하여 '('이면 스택에 저장
* 3. '('이 아닐 때 (')'일 때) 스택에서 '('를 pop시켜 짝을 지어줌
* 4. '('이 아닐 때 (')'일 때) 스택이 비어있다면 짝을 지을 수 없으므로 즉시 false 반환
* 5. 전체 순회 종료 후, 스택이 비어있으면 괄호가 모두 올바르게 짝지어진 것이므로 true 반환, 비어있지 않으면 괄호가 모두 올바르게 짝지어진 것이 아니므로 false 반환
*/
import java.util.*;

class Solution {
    boolean solution(String s) {
        ArrayDeque<Character> stack = new ArrayDeque<>();
        boolean answer = true;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.add(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.isEmpty();
    }
}