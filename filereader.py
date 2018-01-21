#! /usr/bin/python

import sys
import csv

print('The program starts here ')
prog_name = sys.argv.pop(0)

print('Program name :  {}'.format(prog_name))
print('No of arguments passed : {}'.format(len(sys.argv)))
print('Arguments passed to program : {}'.format(sys.argv))

try:
    with open(sys.argv[0]) as f:
        header = f.readline()
        dilect = csv.Sniffer().sniff(header)
        delim = dilect.delimiter
        lineterm = dilect.lineterminator
        h_row = header.strip(lineterm).split(delim)
        data = f.readlines()

except IOError as e:
    print(e)
    print('USAGE : python {} <filename> '.format(prog_name))
    exit(0)

while True:
    print('''SELECT USER OPTIONS FOR READING FILE 
            1. Read file header
            2. Read nth row of file data
            3. Read nth field or fiel data
            4. Read all filedata
            5. EXIT ''')

    
    v1 = raw_input('Enter option here :')
    try:
        if int(v1)==1:
            print('SELECTED OPTION 1: Read file header')
            print('HEADER ROW : {} \n'.format(h_row))
    
        elif int(v1)==2:
            print('SELECTED OPTION 2: Read nth row of the fiel data')
            v2 = raw_input('Enter the row_no, MAX-{} : '.format(len(data)))
            row = data[int(v2)-1]
            if int(v2)!=0:
                print('ROW-{} data : {} \n'.format(v2,row.strip(lineterm).split(delim)))
            else:
                raise ValueError('Enter valid row_no, 1 to MAX-{}'.format(len(data)))

        elif int(v1)==3:
            print('SELECTED OPTION 3: Read nth field data from file')
            v3 = raw_input('Enter field_no to read data, MAX - {} : '.format(len(h_row)))
            if int(v3)!=0:
                fields = [x.strip(lineterm).split(delim)[int(v3)-1] for x in data]
                print('FIELD-{}({}) data : {} \n'.format(v3, h_row[int(v3)-1], fields))
            else:
                raise ValueError('Enter vali field_no, 1 to MAX-{}'.format(len(h_row)))

        elif int(v1)==4:
            print('SELECTED OPTION 4: Read all recods from table data')
            print('TABLE DATA :')
            for i in data:
                print(i.strip(lineterm).split(delim))
            print(lineterm)
        
        elif int(v1)==5:
            exit(0)
        else:
            raise ValueError('Enter valid option (1 to 5)')

    except Exception as e:
        print('Exception/Error : {} \n'.format(e))


