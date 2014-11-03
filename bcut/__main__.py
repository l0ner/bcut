#!/usr/bin/env python3
#
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
import argparse
import fileinput

from textwrap import dedent
    
from .parseFields import ParseFields
from .parseFields import complement
from .cutLine import cutBytes

def parseArgs(inArgs):

    modes = [
        (('-b', '--bytes'), 
            {'action': ParseFields, 'dest': 'range', 'metavar': 'LIST',
                'help': 'display only these bytes' } ),
        (('-c', '--characters'), 
            {'action': ParseFields, 'dest': 'range', 'metavar': 'LIST',
                'help': 'display only these characters' } ),
        (('-f', '--fields'), 
            {'action': ParseFields, 'dest': 'range', 'metavar': 'LIST',
                'help': """select only these fields; also print any line that 
                           contains no delimiter character, unless the -s 
                           option is specified""" } ),
    ]

    arguments = [
        (("-d", '--delimiter'), 
            {'metavar': 'DELIM', 'nargs': 1,
                'help': "use DELIM instead of TAB for field delimiter" } ),
        (("-n", '--no-byte-split'), 
            {'action': 'store_true', 
                'help': "do not slit multi-byte characters (ignored)" } ),
        (('-C', "--complement"), 
            {'action': 'store_true', 
                'help': "complement the set of bytes, characters or fields" } ),
        (('-i', '--invert'), 
            {'action': 'store_true', 
                'help': "count bytes, characters, or fields from the end." } ),
        (('-s', '--only-delimited'), 
            {'action': 'store_true', 
                'help': "do not print lines not containing delimiters" } ),
        (('-O', '--output-delimiter'), 
            {'metavar': 'DELIM', 
                'help': """use DELIM as the output delimiter. The default is to 
                           use the input delimiter""" } )
    ]


    parser = argparse.ArgumentParser(
        prog="bcut", # default argv[0]
        # custom usage string, this is usuallly auto-generated
        #usage="cut OPTION... [FILE]...",
        # app description
        description=dedent("""\
            Print selected parts of lines from each FILE to standard output.
            """), 
        # this will display after help
        epilog=dedent("""\
        Use one, and only one of -b, -c or -f.  Each LIST is made up of one
        range, or many ranges separated by commas.  Selected input is written
        in the same order that it is read, and is written exactly once.
        Each range is one of:
        
          N     N'th byte, character or field, counted from 1
          N-    from N'th byte, character or field, to end of line
          N-M   from N'th to M'th (included) byte, character or field
          -M    from first to M'th (included) byte, character or field
                
        With no FILE, or when FILE is -, read standard input.
                
        bcut home page: <http://www.github.com/l0ner/bcut/>
        For complete documentation, run: man bcut
                """),
        formatter_class=argparse.RawDescriptionHelpFormatter
        )

    # add mode switches
    lists = parser.add_mutually_exclusive_group(required=True)
    for arg, opts in modes:
        lists.add_argument(*arg, **opts)

    # add optional arguments
    for arg, opts in arguments:
        parser.add_argument(*arg, **opts)
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('files', nargs='*', default='-', 
            help="""List of input FILEs to be processed. If none are specified 
            the input will be taken from stdin""")

    args = parser.parse_args(inArgs)

    # check for conflictiong args
    if args.range['mode'] != 'fields' and args.delimiter != None:
        parser.error('an input delimiter may be specified only when operating '
                     'on fields')
    if args.range['mode'] != 'fields' and args.only_delimited != False:
        parser.error("suppressing non-delimited lines makes sense only when "
                     "operating on fields")

    return args


def main():
    args = parseArgs(sys.argv[1:])
    print(args)

    if args.complement:
        args.range['ranges'] = complement(args.range['ranges'])
    
    if args.range['mode'] == 'bytes':
        print('Bytes mode!')
        with fileinput.FileInput(files=args.files, mode='rb') as f:
            for line in f:
                #print("{:0>2}: {}".format(f.lineno(), line))
                print(cutBytes(line, args.range['ranges'], args.complement,
                    args.invert).decode())
    elif args.range['mode'] == 'chars':
        print("Characters!")
    else:
        print("Fields!")


if __name__ == '__main__':
    sys.exit(main())
