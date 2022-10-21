	
import difflib
import sys
#update file pathe

file1 = 'C:/temp/PyTest/new.txt'
file2 = 'C:/temp/PyTest/old.txt'

# git-styled output
with open(file1, 'r') as hosts0:
    with open(file2, 'r') as hosts1:
        diff = difflib.unified_diff(
            hosts0.readlines(),
            hosts1.readlines(),
            fromfile='hosts0',
            tofile='hosts1',
        )
        for line in diff:
            sys.stdout.write(line)
			