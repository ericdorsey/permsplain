#!/usr/bin/env python
from __future__ import print_function  # Force use print()
import subprocess
import sys

if len(sys.argv) > 1:
    argument = sys.argv[1]
    #print("argument was {0}".format(argument))
    popen_call = ["ls", "-l", str(argument)]
else:
    popen_call = ["ls", "-l"]

#list_output = subprocess.Popen(["ls", "-l", "{0}".format(argument)], stdout=subprocess.PIPE).communicate()
list_output = subprocess.Popen(popen_call, stdout=subprocess.PIPE).communicate()

# print(list_output)
list_output = list(list_output)
# print("")
list_output = list_output[:-1]
# print(list_output)
# print("")

list_output = list_output[0].split("\n")
list_output.pop()
if list_output[0].startswith("total"):
    list_output.pop(0)
print("")
for i in list_output:
    print(i)