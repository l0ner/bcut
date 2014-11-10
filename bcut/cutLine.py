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

''' Cutting functions '''

def cutBytes(data, ranges, invert=False):
    out = bytes()
    if invert:
        data = reverseData(data)
    for rng in ranges:
        if rng['start'] <= len(data):
            if rng['end'] == 0 or rng['end'] > len(data):
                end = len(data)
            else:
                end = rng['end']
            out += data[rng['start']-1:end]
    if invert:
        out = reverseData(out)
    return out

def cutChr(data, ranges, invert=False):
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

