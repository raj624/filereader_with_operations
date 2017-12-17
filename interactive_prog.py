#! /usr/bin/python
import sys
import csv

print('The program starts here...!!')
program_name=sys.argv.pop(0)

print('Name of the program : {}'.format(program_name))
print('List of all the parameters passed : {}'.format(len(sys.argv)))
print('Passed arguments are : {}\n'.format(sys.argv))

try:
    with open(sys.argv[0]) as f:
        header = f.readline()
        dilect = csv.Sniffer().sniff(header)
        delim = dilect.delimiter
        lineterm = dilect.lineterminator
        h_row = header.strip(lineterm).split(delim)
        data = f.readlines()
        print(delim, lineterm)

except IOError as e:
    print(e)
    print('USAGE : python {} <FileName>\n'.format(program_name))
    exit(0)

while True:
    print('''SELECT USER OPERATION :
            1. Read file header
            2. Read nth row data
            3. Read nth field data
            4. Read all records
            5. QUIT''')
    v1=raw_input('Enter your option here : ')
    try:
        if int(v1)==1:
            print('SELECTED OPTION 1: Read file header')
            print('HEADER ROW : {} \n'.format(h_row))
        elif int(v1)==2:
            print('SELECTED OPTION 2: Read nth row data')
            v2 = raw_input('Enter row_no to read, MAX-{} :-> '.format(len(data)))
            if int(v2) != 0:
                row = data[int(v2)-1]
                print('ROW-{} data : {} \n'.format(v2, row))
            else:
                raise ValueError('Enter valid row_no to read, 1 to MAX-{}\n '.format(len(data)))
        elif int(v1)==3:
            print('SELECTED OPTION 3: Read nth field data')
            v3 = raw_input('Enter field_no to read, MAX-{} :-> '.format(len(h_row)))
            if int(v3) != 0:
                fields = [x.strip(lineterm).split(delim)[int(v3)-1] for x in data]
                print('FIELD-{} data : {} \n'.format(v3, fields))
            else:
                raise ValueError('Enter valid field_no to read, 1 to MAX-{}'.format(len(h_row)))
        elif int(v1)==4:
            print('SELECTED OPTION 4: Read all records')
            print('TABLE DATA as below :')
            for i in data:
                print(i.strip(lineterm).split(delim))
            print(lineterm)
        elif int(v1)==5:
            exit(0)
    except Exception as e:
        print('Exception/Error : {} \n'.format(e))

