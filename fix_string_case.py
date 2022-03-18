def matching(l1, l2):
    # Returns the number of matching corresponding elements of l1 and l2
    return sum(e1 == e2 for e1, e2 in zip(l1, l2))


def solve(s):
    return s.lower() if matching(s, s.upper()) <= matching(s, s.lower()) else s.upper()


if __name__ == '__main__':

    assert solve("code") == "code"
    assert solve("CODe") == "CODE"
    assert solve("COde") == "code"
    assert solve("Code") == "code"
