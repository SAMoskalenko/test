def flatten(d):
    d1 = {}
    for el in d:
        k = el
        v = d[k]
        if isinstance(v, dict):
            for e in v:
                k1 = e
                v1 = v[e]

                if isinstance(v1, dict):
                    kx = k + '.' + k1
                    res = flatten(v1)
                    for e1 in res:
                        k2 = e1
                        v2 = res[e1]
                        if isinstance(v2, dict):
                            flatten(v2)
                        else:
                            d1[kx + '.' + k2] = v2
                else:

                    d1[k + '.' + k1] = v1
        else:
            d1[k] = v
    return d1


data = {
    "a": 5,
    "b": 6,
    "c": {
        "f": 9,
        "g": {
            "m": 17,
            "n": 3
        },
        "u": 6,
        "r": {
            "m": 17,
            "n": 3,
            "g": {
                "m": 17,
                "n": 3
            }
        },
    }
}

print(flatten(data))
