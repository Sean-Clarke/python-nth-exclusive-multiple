# Given n, and any number of prime factors, returns the nth highest multiple
# constructed exclusively from the given prime factors

def nth_exclusive_multiple(n, *factors):
    if n == 0:
        return 1
    lists = []
    for _f in factors:
        f = [_f, _f]
        lists.append(f)
    for i in range (0, n-2):
        for li in lists:
            other_lists = [ol for ol in lists if ol != li]
            my_turn = True
            for ol in other_lists:
                if li[0] >= ol[0]:
                    my_turn = False
                    break
            if my_turn == True:
                temp = li[0]
                for ol in lists:
                    if lists.index(ol) >= lists.index(li):
                        origin = ol.pop()
                        ol.append(temp * origin)
                        ol.append(origin)
                li.remove(temp)
                break

    for li in lists:
        other_lists = [ol for ol in lists if ol != li]
        lowest = True
        for ol in other_lists:
            if li[0] > ol[0]:
                lowest = False
                break
        if lowest == True:
            return li[0]
