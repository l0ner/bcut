

def cutLine(data, mode, ranges, complement, invert, sep='\t'):
    """Return selected bytes/characters/fields from data

    Positional arguments:
    data - data to be processed <string>
    mode - mode to use <string>
    ranges - ranges to extract from data
    complement - invert selection mask
    invert - count data from the end
    sep - separator to use (default <TAB>) <string>
    """
