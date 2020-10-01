########################### ex1 #######################
composers={'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}
# sorted_composers=sorted(composers.items(), key=lambda el: el[1])

def sort_dict_by_value(d):
    # return {k: v for k, v in sorted(d.items(), key=lambda el: el[1])}
    return dict(sorted(d.items(), key=lambda el: el[1]))

print(sort_dict_by_value(composers))


########################### ex2 #######################
d1={'a':1, 'b':2, 'c':3, 'd':4}
d2={'b':20, 'c':30, 'y':40, 'z':50}

def intersect(d1, d2):
    d1_keys=d1.keys()
    d2_keys=d2.keys()
    keys=d1_keys & d2_keys
    return {k: (d1[k], d2[k])for k in keys}

print(intersect(d1, d2))
