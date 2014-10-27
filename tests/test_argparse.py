import bcut

import unittest

class testArgParser(unittest.TestCase):
    knownRangeResults = ( 
        ( '1',     [{ 'start': 1, 'end': 1 }] ),
        ( '2',     [{ 'start': 2, 'end': 2 }] ),
        ( '2-',    [{ 'start': 2, 'end': 0 }] ),
        ( '1-5',   [{ 'start': 1, 'end': 5 }] ),
        ( '-5',    [{ 'start': 1, 'end': 5 }] ),
        ( '1,3',   [{ 'start': 1, 'end': 1 }, { 'start': 3, 'end': 3 }] ),
        ( '1,2-',  [{ 'start': 1, 'end': 1 }, { 'start': 2, 'end': 0 }] ),
        ( '1,2-5', [{ 'start': 1, 'end': 1 }, { 'start': 2, 'end': 5 }] ),
        ( '1,-5',  [{ 'start': 1, 'end': 1 }, { 'start': 1, 'end': 5 }] ),
        ( '1,2-5,7', [
            { 'start': 1, 'end': 1 }, { 'start': 2, 'end': 5 },
            { 'start': 7, 'end': 7 }
            ] 
        ), ( '1,2-5,7-9', [
            { 'start': 1, 'end': 1 }, { 'start': 2, 'end': 5 },
            { 'start': 7, 'end': 9 }] 
        ), ( '1,2-5,7,9-13', [
            { 'start': 1, 'end': 1 },{ 'start': 2, 'end': 5 },
            { 'start': 7, 'end': 7 },{ 'start': 9, 'end': 13 }] 
        )
    )

    knownModeResults = (
        ( '-b', 'bytes' ),
        ( '-c', 'chars' ),
        ( '-f', 'fields' ),
        ( '--bytes', 'bytes' ),
        ( '--characters', 'chars' ),
        ( '--fields', 'fields' )
    )

    ranges = [
        { 'start': 1,  'end': 5  },
        { 'start': 3,  'end': 3  },
        { 'start': 8,  'end': 10 },
        { 'start': 9,  'end': 12 },
        { 'start': 15, 'end': 20 },
        { 'start': 16, 'end': 19 },
        { 'start': 25, 'end': 25 },
        { 'start': 27, 'end': 30 },
        { 'start': 28, 'end': 0  }
    ]

    sortedRanges = [
        { 'start': 1,  'end': 5  },
        { 'start': 8,  'end': 12 },
        { 'start': 15, 'end': 20 },
        { 'start': 25, 'end': 25 },
        { 'start': 27, 'end': 0  }
    ]


    def test_ranges(self):
        '''parseArgs should parse ranges correctly'''
        for rangeStr, expectedResult in self.knownRangeResults:
            ranges = bcut.parseArgs(['-b', rangeStr])
            self.assertEqual(expectedResult, ranges.range['ranges'])

    def test_modes(self):
        '''parseArgs should return cutting mode. Either bytes/chars/fields'''
        for mode, expectedResult in self.knownModeResults:
            modeResult = bcut.parseArgs([mode, '1'])
            self.assertEqual(expectedResult, modeResult.range['mode'])

    def test_sorting(self):
        '''sortRanges should return ranges sorted by start and remove 
           overlapping ones'''
        self.ranges = bcut.handleRanges.sortRanges(self.ranges)
        self.assertEqual(self.sortedRanges, self.ranges)

class badArgParse(unittest.TestCase):
    failingRanges = [ '10-5', 'N', 'n-', '=-n', 'a-n', '0-8', '0' ]
    def test_too_large(self):
        '''parseArgs shoud fail with incorrect ranges'''
        for badRange in self.failingRanges:
            self.assertRaises(ValueError, bcut.parseArgs, ['-b', badRange])

if __name__ == '__main__':
    unittest.main()


