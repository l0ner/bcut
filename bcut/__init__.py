#!/usr/bin/env python3
#
####################################################################
#
# __init__.py
#
# Copyright (C) 2014 Pawel 'l0ner' Soltys <pwslts@gmail.com>
#
# bcut is free software.
#
# You may redistribute it and/or modify it under the terms of the
# GNU General Public License, as published by the Free Software
# Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# bcut is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with bcut.    If not, write to:
#   The Free Software Foundation, Inc.,
#   51 Franklin Street, Fifth Floor
#   Boston, MA  02110-1301, USA.
#
####################################################################

import sys
import argparse

from textwrap import dedent

class ParseFields(argparse.Action):
    def splitRange(rng):
        val = rng.split('-')
        if not val[0].isdigit() or not val[1].isdigit():
            raise ValueError("Argument is not a number")
        beg = int(val[0]) if val[0] != '' else 0
        end = int(val[1]) if val[1] != '' else 0
        return { 'start': beg, 'end': end }
    def fieldParse(field):
        if '-' in field:
            return self.splitRange(field)
        else:
            if field.isdigit():
                return { 'start': int(field), 'end': int(field) }
            else:
                raise ValueError("Argument is not a number")
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super(ParseFields, self).__init__(option_strings, dest, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        if ',' in values:
            values = values.split(',')
            for i in range(len(values)):
                values[i] = self.fieldParse(field=values[i])
        else:
            values = self.fieldParse(field=values)
        setattr(namespace, self.dest, values)

def parseArgs():
    parser = argparse.ArgumentParser(
        prog="bcut", # default argv[0]
        # custom usage string, this is usuallly auto-generated
        usage="cut OPTION... [FILE]...",
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
        Report bcut translation bugs to <http://translationproject.org/team/>
        For complete documentation, run: man bcut
                """),
        formatter_class=argparse.RawDescriptionHelpFormatter
        )
    lists = parser.add_mutually_exclusive_group(required=True)
    lists.add_argument("-b", "--bytes", 
            action=ParseFields,
            help="display only these bytes",
            metavar='LIST')
    lists.add_argument("-c", "--characters",
            action=ParseFields,
            help="display only these characters",
            metavar='LIST')
    lists.add_argument("-f", "--fields", 
            action=ParseFields,
            help="""select only these fields; also print any line that contains 
                    no delimiter character, unless the -s option is specified
                    """,
            metavar='LIST')
    parser.add_argument('-d', '--delimiter', nargs=1, metavar='DELIM',
            help="use DELIM instead of TAB for field delimiter")
    parser.add_argument('-n', action='store_true',
            help="Do not split multi-byte characters (no-op for now).")
    parser.add_argument('--complement', action='store_true',
            help="Complement the set of selected bytes, characters or fields")
    parser.add_argument('-i', '--invert', action='store_true',
            help="Count butes, characters or fields from the end of the string")
    parser.add_argument('-s', '--only-delimited', action='store_true',
            help="do not print lines not containing delimiters")
    parser.add_argument('--output-delimiter', metavar='STRING',
            help="""use STRING as the output delimiter. The default is to use
                    the inpt delimiter""")
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('files', nargs='*', default='-', 
            help="""List of input FILEs to be processed. If none are specified 
            the input will be taken from stdin""")

    return parser.parse_args()


def main():
    args = parseArgs()
    print(args)

    '''with args.file as f:
        for line in f:
            print(line, end='')'''

if __name__ == '__main__':
    sys.exit(main())
