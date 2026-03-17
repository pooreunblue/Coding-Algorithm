from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    current_weight = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0 * n for n in range(bridge_length)])
    while bridge:
        w = bridge.popleft()
        current_weight -= w
        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                t = truck_weights.popleft()
                current_weight += t
                bridge.append(t)
            else:
                bridge.append(0)
        time += 1
    return time