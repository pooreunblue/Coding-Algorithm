/**
* 마찬가지로 이전에 파이썬으로 풀어보았던 문제인지라 자바로 다시 처음부터 풀이하였습니다.
* 1. 다리를 큐로 구현, 아직 다리에 올라가지 않은 트럭들을 큐로 구현
* 2. 트럭들 큐에 트럭들을 순서대로 투입
* 3. 다리 큐에 0을 다리 길이만큼 채움
* 4. 다리의 원소가 비지 않을 때까지 반복문 수행
* 4-1. 다리의 원소 하나 poll(pop) -> 레일이 한 칸 앞으로 진행하는 것과 같음
* 4-2. 다리의 무게에서 원소 만큼 뺌
* 4-3. 트럭들 큐에 트럭이 있다면, 현재 다리 위의 무게와 맨 먼저 나갈 트럭들의 무게가 견딜 수 있는 무게보다 작다면 트럭들 큐에서 맨 앞 트럭 하나 poll, 그 무게를 다리 위의 무게에 더하고 다리에 poll한 트럭 offer
* 4-4. 트럭들 큐에 트럭이 있다면, 현재 다리 위의 무게와 맨 먼저 나갈 트럭들의 무게가 견딜 수 있는 무게보다 크다면 0 offer
* 5. 한 번씩 움직일때마다 time 1씩 증가
*/

import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int time = 0;
        int currentWeight = 0;
        ArrayDeque<Integer> bridge = new ArrayDeque<>();
        ArrayDeque<Integer> truckWeights = new ArrayDeque<>();
        for (int t: truck_weights) {
            truckWeights.add(t);
        }
        for (int i = 0; i < bridge_length; i++) {
            bridge.offer(0);
        }
        while (!bridge.isEmpty()) {
            int w = bridge.poll();
            currentWeight -= w;
            if (!truckWeights.isEmpty()) {
                if (currentWeight + truckWeights.peekFirst() <= weight) {
                    int weights = truckWeights.poll();
                    currentWeight += weights;
                    bridge.offer(weights);
                } else {
                    bridge.offer(0);
                }
            }
            time += 1;
        }
        return time;
    }
}