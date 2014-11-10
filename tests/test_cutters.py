from bcut import cutLine

import unittest

class testDataCutters(unittest.TestCase):
    byte = b'abcdefghijklmnopqrstuvwxyz'
    chars = 'abcdefghijklmnopqrstuvwxyz'
    ranges = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    knownByteResults = (
        ( [ { 'start': 1, 'end': 1 } ], b'a' ),
        ( [ { 'start': 5, 'end': 5 } ], b'e' ),
        ( [ { 'start': 1, 'end': 5 } ], b'abcde' ),
        ( [ { 'start': 5, 'end': 0 } ], b'efghijklmnopqrstuvwxyz' ),
        ( [ { 'start': 5, 'end': 5 }, { 'start': 7, 'end': 7 } ], b'eg' ),
        ( [ { 'start': 5, 'end': 5 }, { 'start': 7, 'end': 0 } ],
            b'eghijklmnopqrstuvwxyz' ),
        ( [ { 'start': 1, 'end': 1 }, { 'start': 8, 'end': 8 },
            { 'start': 12, 'end': 14 } ], b'ahlmn' )
    )
    knownCharNFieldResults = (
        ( [ { 'start': 1, 'end': 1 } ], 'a' ),
        ( [ { 'start': 5, 'end': 5 } ], 'e' ),
        ( [ { 'start': 1, 'end': 5 } ], 'abcde' ),
        ( [ { 'start': 5, 'end': 0 } ], 'efghijklmnopqrstuvwxyz' ),
        ( [ { 'start': 5, 'end': 5 }, { 'start': 7, 'end': 7 } ], 'eg' ),
        ( [ { 'start': 5, 'end': 5 }, { 'start': 7, 'end': 0 } ],
            'eghijklmnopqrstuvwxyz' ),
        ( [ { 'start': 1, 'end': 1 }, { 'start': 8, 'end': 8 },
            { 'start': 12, 'end': 14 } ], 'ahlmn' )
    )

    def test_byte_cutter(self):
        '''cutBytes should return only selected bytes'''
        for ranges, expected in self.knownByteResults:
            result = cutLine.cutBytes(self.byte, ranges)
            self.assertEqual(expected, result)

    def test_charaters_cutter(self):
        '''cutChr should return only selected characters'''
        for ranges, expected in self.knownCharNFieldResults:
            result = cutLine.cutChr(self.chars, ranges)
            self.assertEqual(expected, result)

    def test_field_cutter(self):
        '''cutFields should return only selected fields'''
        for ranges, expected in self.knownCharNFieldResults:
            result = cutLine.cutFields(self.ranges, ranges)
            result = ''.join(result)
            self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
