from bcut import parseArgs

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
        ( '1,-5',  [{ 'start': 1, 'end': 5 }] ),
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
        ), ( '1-5,3,8-10,9-12,15-20,16-19,25,27-30,28-', [
            { 'start': 1,  'end': 5  },
            { 'start': 8,  'end': 12 },
            { 'start': 15, 'end': 20 },
            { 'start': 25, 'end': 25 },
            { 'start': 27, 'end': 0  }]
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

    def test_ranges(self):
        '''parseArgs should parse ranges correctly'''
        for rangeStr, expectedResult in self.knownRangeResults:
            ranges = parseArgs.parseArgs(['-b', rangeStr])
            self.assertEqual(expectedResult, ranges.range['ranges'])

    def test_modes(self):
        '''parseArgs should return cutting mode. Either bytes/chars/fields'''
        for mode, expectedResult in self.knownModeResults:
            modeResult = parseArgs.parseArgs([mode, '1'])
            self.assertEqual(expectedResult, modeResult.range['mode'])

class badArgParse(unittest.TestCase):
    failingRanges = [ '10-5', 'N', 'n-', '=-n', 'a-n', '0-8', '0' ]
    def test_too_large(self):
        '''parseArgs shoud fail with incorrect ranges'''
        for badRange in self.failingRanges:
            self.assertRaises(ValueError, parseArgs.parseArgs, ['-b', badRange])

if __name__ == '__main__':
    unittest.main()


