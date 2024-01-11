#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv)
    i = 1
    
    if argc == 1:
        print('0 arguments.')
    elif argc == 2:
        print('{} argument: {}'.format((argc - 1), argv[i]))
    else:
        print('{} arguments:'.format(argc - 1))
        while i < argc:
            print('{}: {}'.format(i, argv[i]))
            i = i + 1
