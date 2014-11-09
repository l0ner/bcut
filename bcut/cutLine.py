def cutBytes(data, ranges, invert=False):
    out = bytes()
    if invert:
        data = reverseData(data)
    for rng in ranges:
        if rng['start'] <= len(data):
            if rng['end'] == 0 or rng['end'] > len(data):
                end = len(data) - 1
            else:
                end = rng['end']
            out += data[rng['start']-1:end]
    if invert:
        out = reverseData(out)
    return out

def cutStr(data, ranges, invert=False):
    out = str()
    if invert:
        data = reverseData(data)
    for rng in ranges:
        if rng['start'] < len(data):
            if rng['end'] == 0 or rng['end'] > len(data):
                end = len(data)
            else:
                end = rng['end']
            out += data[rng['start']-1:end]
    if invert:
        out = reverseData(out)
    return out

def cutFields(data, ranges, invert=False):
    out = list()
    if invert:
        data = reverseData(data)
    for rng in ranges:
        if rng['start'] <= len(data):
            if rng['end'] == 0 or rng['end'] > len(data):
                end = len(data)
            else:
                end = rng['end']
            for i in range(rng['start'] - 1, end):
                out.append(data[i])
    if invert:
        out = reverseData(out)
    return out

def reverseData(data):
    return data[::-1]
