#! /usr/bin/python
import sys

print('The program starts here...!!')
program_name=sys.argv.pop(0)

print('Name of the program : {}'.format(program_name))

print('List of all the parameters passed : {}'.format(len(sys.argv)))

print('Passed arguments are : {}'.format(sys.argv))

try:
    with open(sys.argv[0]) as f:
        print(f.readline())
        for line in f.readlines():
            print(line.strip())
except IndexError as ind:
    print('Enter valid file name, {}'.format(ind))
except IOError as e:
    print('Enter valid file name, {}'.format(e))
