####################################################################
#
# bcut - a better cut utility
#
# Copyright (C) 2014 Pawel 'l0ner' Soltys <pwslts@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##########################################################################

''' ParseFields argprase cutom action '''

from argparse import Action

class ParseFields(Action):
    def splitRange(self, rng):
        val = rng.split('-')
        if val[0] != '' and not val[0].isdigit():
            raise ValueError("Argument is not a number")
        if val[1] != '' and not val[1].isdigit():
            raise ValueError("Argument is not a number")
        if val[0] == '0':
            raise ValueError("fields and positions are numbered from 1")
        if ( val[0] != '' and val[1] != '' ) \
                and int(val[0]) > int(val[1]):
            raise ValueError("Range beginning bigger than end")
        return { 'start': int(val[0]) if val[0] != '' else 1, 
                 'end': int(val[1]) if val[1] != '' else 0 }

    def parseField(self, field):
        if '-' in field:
            return self.splitRange(field)
        else:
            if field.isdigit():
                if field == '0':
                    raise ValueError("fields and positions are numbered from 1")
                return { 'start': int(field), 'end': int(field) }
            else:
                raise ValueError("Argument is not a number")

    def sortRanges(self, l):
        '''returns sorted and non-overlapping ranges'''
        l = sorted(l, key=lambda rng: rng['start'])
        i = 0
        length = len(l) - 1
        while i < length:
            if l[i]['end'] >= l[i+1]['start']:
                if l[i+1]['end'] == 0 or l[i+1]['end'] > l[i]['end']:
                    # next item starts within current, but ends outside. append
                    l[i]['end'] = l[i+1]['end']
                del l[i+1]
                length -= 1
            i += 1
        return l

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super(ParseFields, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if option_string == '-b' or option_string == '--bytes':
            mode = { 'mode': 'bytes' }
        elif option_string == '-c' or option_string == '--characters':
            mode = { 'mode': 'chars' }
        elif option_string == '-f' or option_string == '--fields':
            mode = { 'mode': 'fields' }
        else:
            raise ValueError("Critical: Unknown mode! Should be -b/-c/-f")

        if ',' in values:
            split_values = values.split(',')
            for i in range(len(split_values)):
                split_values[i] = self.parseField(split_values[i])
            mode['ranges'] = self.sortRanges(split_values)
        else:
            # only one item in range
            mode['ranges'] = list()
            mode['ranges'].append(self.parseField(values))
        
        values = mode
        setattr(namespace, self.dest, values)

def complement(ranges):
    out = list()
    length = len(ranges)
    if length < 2:
        # only one range
        if ranges[0]['start'] == 1:
            # first fields
            if ranges[0]['end'] == 0:
                # special case, complement is empty
                return out
            else:
                start = ranges[0]['end'] + 1
                end = 0
                out.append({ 'start': start, 'end': end })
        else:
            # middle or end fields
            out.append({ 'start': 1, 'end': ranges[0]['start'] - 1 })
            if ranges[0]['end'] != 0:
                # range ends before fields end
                out.append({ 'start': ranges[0]['end'] + 1, 'end': 0 })
    else:
        # more than one range
        i = 0
        while i < length:
            if i == 0:
                # check first range
                if ranges[i]['start'] != 1:
                    #we need begining range
                    out.append({ 'start': 1, 'end': ranges[i]['start'] - 1 })
                
            # process field
            if i < length - 1:
                end = ranges[i+1]['start'] - 1
            else:
                end = 0
            
            if ranges[i]['end'] != 0:
                start = ranges[i]['end'] + 1
                out.append({ 'start': start, 'end': end })

            i += 1

    return out
