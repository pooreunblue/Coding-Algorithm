def solution(record):
    directory = {}
    log = {}
    a = []
    for r in record:
        data = r.split()
        if data[0] == "Enter" or data[0] == "Change":
            directory[data[1]] = data[2]
    for r in record:
        data = r.split()
        if data[0] == "Enter":
            a.append(directory[data[1]]+"님이 들어왔습니다.")
        elif data[0] == "Leave":
            a.append(directory[data[1]]+"님이 나갔습니다.")
    return a