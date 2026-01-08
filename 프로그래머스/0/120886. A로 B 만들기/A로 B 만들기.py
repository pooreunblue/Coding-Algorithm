def solution(before, after):
    for c in before:
        if c in after:
            after = after.replace(c, '', 1)
    if len(after) == 0:
        return 1
    return 0