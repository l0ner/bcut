import bcut

import unittest

class testRanges(unittest.TestCase):
    knownResults = ( 
            ( '1',     [{ 'start': 1, 'end': 1 }] ),
            ( '2',     [{ 'start': 2, 'end': 2 }] ),
            ( '2-',    [{ 'start': 2, 'end': 0 }] ),
            ( '1-5',   [{ 'start': 1, 'end': 5 }] ),
            ( '-5',    [{ 'start': 0, 'end': 5 }] ),
            ( '1,3',   [{ 'start': 1, 'end': 1 }, { 'start': 3, 'end': 3 }] ),
            ( '1,2-',  [{ 'start': 1, 'end': 1 }, { 'start': 2, 'end': 0 }] ),
            ( '1,2-5', [{ 'start': 1, 'end': 1 }, { 'start': 2, 'end': 5 }] ),
            ( '1,-5',  [{ 'start': 1, 'end': 1 }, { 'start': 0, 'end': 5 }] ),
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

    def test_ranges(self):
        '''parseArgs should parse ranges correctly'''
        for rangeStr, expectedResult in self.knownResults:
            ranges = bcut.parseArgs(['-b', rangeStr]).range['ranges']
            self.assertEqual(expectedResult, ranges)

if __name__ == '__main__':
    unittest.main()


