#!/usr/bin/python3
from sys import argv

argc = len(argv)
i = 1
if argc == 1:
    print('0 arguments.'.format(argc))
else:
    print('{} arguments:'.format(argc - 1))
    while i < argc:
        print('{}: {}'.format(i, argv[i]))
        i = i + 1
