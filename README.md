# Permsplain

For `ls -la` output on Linux, Unix, or OSX, explains permissions for files and directories.

## Usage

#### Explain permissions for just one file:

```
$ ~/Code/Permsplain/./permsplain.py index.html

-rw-r--r--  1 ericdorsey  staff  0 Apr 21 21:04 index.html
File type: Regular file
Owner permissions: read write
Group permissions: read
Other permissions: read
Number of hard links: 1
Owner: ericdorsey
Belongs to group: staff
File size in blocks: 0
File last modified: Apr 21 21:04
File name: index.html

```

#### Explain permissions for just one directory:

```
$ ~/Code/Permsplain/./permsplain.py js/

drwxr-xr-x  2 ericdorsey  staff  68 Apr 21 21:04 js/
File type: Directory
Owner permissions: read write execute
Group permissions: read execute
Other permissions: read execute
Number of hard links: 2
Owner: ericdorsey
Belongs to group: staff
File size in blocks: 68
File last modified: Apr 21 21:04
File name: js/
```

#### Or, run it without any arguments to explain permissions for every file in the current directory:

```
$ ~/Code/Permsplain/./permsplain.py

-rw-r--r--   1 ericdorsey  staff    0 Apr 21 21:04 index.html
File type: Regular file
Owner permissions: read write
Group permissions: read
Other permissions: read
Number of hard links: 1
Owner: ericdorsey
Belongs to group: staff
File size in blocks: 0
File last modified: Apr 21 21:04
File name: index.html

drwxr-xr-x   2 ericdorsey  staff   68 Apr 21 21:04 js
File type: Directory
Owner permissions: read write execute
Group permissions: read execute
Other permissions: read execute
Number of hard links: 2
Owner: ericdorsey
Belongs to group: staff
File size in blocks: 68
File last modified: Apr 21 21:04
File name: js

-rw-r--r--   1 ericdorsey  staff    0 Apr 21 21:04 more.html
File type: Regular file
Owner permissions: read write
Group permissions: read
Other permissions: read
Number of hard links: 1
Owner: ericdorsey
Belongs to group: staff
File size in blocks: 0
File last modified: Apr 21 21:04
File name: more.html

drwxr-xr-x   2 ericdorsey  staff   68 Apr 21 21:04 records
File type: Directory
Owner permissions: read write execute
Group permissions: read execute
Other permissions: read execute
Number of hard links: 2
Owner: ericdorsey
Belongs to group: staff
File size in blocks: 68
File last modified: Apr 21 21:04
File name: records
```
____

#### Optional Convenience Usage

If you don't wan't to have to type the full path to `permsplain.py` on every usage, you can add to `$PATH` for usage like this:

Add the following to your `.bash_profile`:

```
# For permsplain
export PATH=$PATH:/Full/path/to/Permsplain

```

Then restart Terminal, and run like this:

```
$ permsplain.py index.html
```
