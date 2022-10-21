import sys

import re
  

inpu_file = open(r"C:\temp\PyTest\Castor_variables_04Aug2022.csv", "r").read()

for line in re.findall("srv.....", inpu_file):
    print(line)