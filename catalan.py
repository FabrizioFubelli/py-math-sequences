#!/usr/bin/env python2

"""
Calculates the nth Catalan number
"""

import sys

# Show usage
def usage():
    print("Usage: "+str(sys.argv[0])+" [OPTION] <number>")
    print("Calculetes the nth catalan number")
    print("Options:")
    print("  -a, --all                  show all calculated numbers (till <number>)")
    print("  -v, --verbose              show verbose output. Ex: C(n) = result")

# Calculates the nth Catalan number
def catalan(n):
    c = 0
    if n == 0: return 1
    else:
        for i in range(n): c += (catalan(i))*(catalan(n-1-i))
    return c

# Validate and get the arguments
# @return dict A dictionary that contains the arguments as {'arg_name': True|False}
def get_args():
    args = {'all': False, 'verbose': False}
    args_tr = {
        '-a': 'all', '--all': 'all',
        '-v': 'verbose', '--verbose': 'verbose'
    }
    number = None
    for arg in sys.argv[1:]:
        arg_tr = args_tr.get(arg)
        if (arg_tr == None):
            try:
                number = int(arg)
            except ValueError:
                print('Invalid argument: '+str(arg))
                usage()
                exit(2)
        args[arg_tr] = True
    if (number == None):
        usage()
        exit(3)
    return args, number

# The main function
def main():
    if (len(sys.argv) < 2):
        usage()
        exit(1)
    args, number = get_args()
    if (args.get('all')):
        for x in range(number+1):
            if (args.get('verbose')):
                print('C('+str(x)+') = '+str(catalan(x)))
            else:
                print(str(catalan(x)))
    else:
        if (args.get('verbose')):
            print('C('+str(number)+') = '+str(catalan(number)))
        else:
            print(str(catalan(number)))

if __name__ == "__main__":
    main()
