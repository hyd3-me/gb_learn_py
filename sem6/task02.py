def check_diag(q1, q2):
    p1 = q1[0] - q1[1]
    p2 = q2[0] - q2[1]
    print(p1, p2)
    if p1 != p2:
        return 0
    else:
        return 1

def is_attacking(q1,q2):
    if q1[0] == q2[0] or q1[1] == q2[1]:
        return False
    if (check_diag(q1, q2)):
        return False
    return True

def check_arr(q1, _list):
    for item in _list:
        state = is_attacking(q1, item)
        if not state:
            return False
    return True

def check_queens(queens):
    if not queens:
        return True
    s1 = queens.pop()
    while queens:
        state = check_arr(s1, queens)
        if not state:
            return False
        s1 = queens.pop()
    return True


if __name__ == '__main__':
    print(check_queens())