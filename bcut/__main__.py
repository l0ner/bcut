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

''' Main starting point for bcut. Contains main() entry point '''

import sys
import fileinput

from .parseArgs import parseArgs
from .parseFields import complement
from .cutLine import cutBytes
from .cutLine import cutStr
from .cutLine import cutFields

def main():
    args = parseArgs(sys.argv[1:])

    if args.complement:
        args.range['ranges'] = complement(args.range['ranges'])
    
    if args.range['mode'] == 'bytes':
        with fileinput.FileInput(files=args.files, mode='rb') as f:
            for line in f:
                print(cutBytes(line, args.range['ranges'],
                    args.invert).decode())
    elif args.range['mode'] == 'chars':
        with fileinput.FileInput(files=args.files, mode='r') as f:
            for line in f:
                print(cutStr(line[:-1], args.range['ranges'],
                    args.invert))
    else:
        with fileinput.FileInput(files=args.files, mode='r') as f:
            for line in f:
                if args.delimiter[0] in line:
                    line = line[:-1].split(args.delimiter[0])
                    line = cutFields(line, args.range['ranges'], args.invert)
                    line = args.delimiter[0].join(line)
                    print(line)
                else:
                    if not args.only_delimited:
                        print(line)

if __name__ == '__main__':
    sys.exit(main())
