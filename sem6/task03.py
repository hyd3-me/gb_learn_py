import random, time


def check_diag(q1, q2):
    p1 = q1[0] - q1[1]
    p2 = q2[0] - q2[1]
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

def gen_position():
    return (random.randint(1, 8), random.randint(1, 8))

def gen_pair():
    state = False
    while not state:
        pos1 = gen_position()
        pos2 = gen_position()
        state = is_attacking(pos1, pos2)
    return (pos1, pos2)

def gen_list():
    _start = time.process_time()
    pair1 = gen_pair()
    _list = []
    _list += pair1
    state = 1
    while state:
        if len(_list) < 8:
            pos = gen_position()
            s = check_arr(pos, _list)
            if s:
                _list.append(pos)
            _end = time.process_time()
            if _end - _start > 1:
                _list = []
                _start = time.process_time()
                pair1 = gen_pair()
                _list += pair1
        else:
            state = 0
    return _list

def make_lists():
    final_list = []
    for _ in range(4):
        final_list.append(gen_list())
    return final_list

def generate_boards():
    queens = make_lists()
    return queens


if __name__ == '__main__':
    generate_boards()