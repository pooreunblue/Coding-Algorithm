from itertools import combinations

def solution(orders, course):
    answer = []
    courses = {}
    counts = {}
    for order in orders:
        for c in course:
            order = sorted(order)
            if len(order) >= c:
                menus = [''.join(menu) for menu in combinations(order,c)]
                for menu in menus:
                    if menu not in courses:
                        courses[menu] = 1
                    else:
                        courses[menu] += 1
    for c in course:
        for menu, count in courses.items():
            length = len(menu)
            if length == c and count > 1:
                if length in counts:
                    if count > counts[length][1]:
                        counts[length] = (menu, count)
                else:
                    counts[length] = (menu, count)
    for length, values in counts.items():
        for menu, count in courses.items():
            if len(menu) == length and count == values[1]:
                answer.append(menu)
    return sorted(answer)