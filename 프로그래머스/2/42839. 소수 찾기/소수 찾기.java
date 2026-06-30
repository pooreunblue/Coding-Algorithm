import java.util.*;

class Solution {
    static Set<Integer> set = new HashSet<>(); // 중복을 제거하여 수를 세기 위한 자료구조
    public int solution(String numbers) {
        boolean[] visited = new boolean[numbers.length()]; // 사용한 숫자인지 체크
        dfs(numbers, visited, ""); // ""부터 종이 조각 붙이기 시작
        int count = 0; // 소수 개수 
        for (int num : set) { // 집합 순회하며 
            if (isPrime(num)) { // 소수인지 체크
                count++; // 소수면 카운트
            }
        }
        return count; // 카운트 증가
    }
    
    static void dfs(String numbers, boolean[] visited, String current) {
        if (!current.equals("")) { // 문자열이 비어있지 않기만 하면
            set.add(Integer.parseInt(current)); // 바로 집합에 저장
        }
        for (int i=0; i < numbers.length(); i++) { // 문자열 모두 순회
            if (visited[i]) continue; // 이미 사용한 숫자 제외
            visited[i] = true; // 사용 여부 체크
            dfs(numbers, visited, current + numbers.charAt(i)); // 다음 숫자 만들기
            visited[i]= false; // 새로운 수 만들때 또 쓸 수 있으므로 원상 복구
        }
    }
    
    static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}