import sys

import re
  

input_file = open(r"C:\Users\nachl\Downloads\srv_list.txt", "r").read()

#for line in re.findall("plm.*", inpu_file):
#   print(line)

word = re.findall("plm.*", input_file)

for i in word:
	print(i)