#!/usr/bin/env python
from __future__ import print_function  # Force use print()
import subprocess
import sys

perm_codes = {
    "r" : "read",
    "w" : "write",
    "x" : "execute",
    "-" : "regular file",
    "d" : "directory",
    "l" : "symbolic link"
}

def perm_parser(
        file_type,
        owner_perms,
        group_perms,
        other_perms,
        number_hard_links,
        owner,
        group_belongs,
        file_size_in_blocks,
        last_modified_time,
        name_of_file_or_dir):
    print("Permissions for: {0}".format(name_of_file_or_dir))
    


if len(sys.argv) > 1:
    argument = sys.argv[1]
    #print("argument was {0}".format(argument))
    #popen_call = ["ls", "-l", str(argument)]
# else:
#     popen_call = ["ls", "-l"]

#list_output = subprocess.Popen(popen_call, stdout=subprocess.PIPE).communicate()
list_output = subprocess.Popen(["ls", "-la"], stdout=subprocess.PIPE).communicate()
print(list_output)
list_output = list(list_output)
list_output = list_output[:-1]
list_output = list_output[0].split("\n")
list_output.pop()
# If more than one file (ie, no argument)
if list_output[0].startswith("total"):
    list_output.pop(0)

# Sanity check
print("")
for i in list_output:
    print(i)
    current_ls_line = i.split()
    print(len(current_ls_line), current_ls_line)
    if len(current_ls_line) == 11:  # symlink
        current_ls_line[8:11] = ["".join(current_ls_line[8:11])]
    print(len(current_ls_line), current_ls_line)
    # Owner, Group, Other
    perms = current_ls_line[0]  # -rwxr-xr-x
    file_type = perms[0]  # -, d, or l
    owner_perms = perms[1:4]
    group_perms = perms[4:7]
    other_perms = perms[7:10]
    number_hard_links = current_ls_line[1]
    owner = current_ls_line[2]
    group_belongs = current_ls_line[3]
    file_size_in_blocks = current_ls_line[4]
    last_modified_month = current_ls_line[5]
    last_modified_day = current_ls_line[6]
    last_modified_time_or_year = current_ls_line[7]
    last_modified_time = "{0} {1} {2}".format(
        last_modified_month,
        last_modified_day,
        last_modified_time_or_year)
    name_of_file_or_dir = current_ls_line[8]
    print("")
    print(name_of_file_or_dir)
    print("Owner permissions: ")


    print("")
print("")