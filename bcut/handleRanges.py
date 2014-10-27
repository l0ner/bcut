def sortRanges(l):
    '''returns sorted and non-overlapping ranges'''
    l = sorted(l, key=lambda rng: rng['start'])
    i = 0
    length = len(l)
    while i < length:
        if l[i]['end'] >= l[i+1]['start']:
            if l[i+1]['end'] == 0 or l[i+1]['end'] > l[i]['end']:
                # next item starts within current, but ends outside. append
                l[i]['end'] = l[i+1]['end']
            del l[i+1]
            length -= 1
        i += 1
    return l
