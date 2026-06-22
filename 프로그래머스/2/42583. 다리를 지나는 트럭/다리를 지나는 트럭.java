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