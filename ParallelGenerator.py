Last login: Thu Nov 14 10:09:41 on ttys000
DanMac:~ dhuth$ cd Desktop/CS_Comps_Parallel/
DanMac:CS_Comps_Parallel dhuth$ git
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   branch     List, create, or delete branches
   checkout    Switch branches or restore working tree files
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   merge      Join two or more development histories together
   rebase     Reapply commits on top of another base tip
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
DanMac:CS_Comps_Parallel dhuth$ git add parallelCall.py 
DanMac:CS_Comps_Parallel dhuth$ git commit -m "Added parallel call"
[master 086197e] Added parallel call
 1 file changed, 15 insertions(+)
 create mode 100644 parallelCall.py
DanMac:CS_Comps_Parallel dhuth$ git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 568 bytes | 568.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Danhuth/CS_Comps_Parallel
   a3e2807..086197e  master -> master
DanMac:CS_Comps_Parallel dhuth$ ssh enigma
dhuth@enigma's password: 
Connection closed by 134.69.66.19 port 22
DanMac:CS_Comps_Parallel dhuth$ workon gap
-bash: workon: command not found
DanMac:CS_Comps_Parallel dhuth$ ls
Output_Collator.py	ParallelGenerator.py
ParallelGapCall.py	parallelCall.py
DanMac:CS_Comps_Parallel dhuth$ cd
DanMac:~ dhuth$ ls
AndroidStudioProjects		PaladinTemp
Applications			Pet.class
Desktop				Pet.java
Documents			Pictures
Downloads			Public
GraphicsComponentV2.class	Zotero
GraphicsComponentV2.java	eclipse
GraphicsFrameV2.class		eclipse-workspace
GraphicsFrameV2.java		get-pip.py
GraphicsPanel1.class		jefflab.class
GraphicsPanel1.java		jefflab.java
Library				matlab_crash_dump.353-1
Movies				matlab_crash_dump.3707-1
Music				matlab_crash_dump.9273-1
DanMac:~ dhuth$ ssh enigma
dhuth@enigma's password: 
Last login: Thu Nov 14 10:09:46 2019 from 134.69.198.240

Your array seems to be healthy
[dhuth@enigma ~]$ workon gap
(gap) [dhuth@enigma ~]$ ls
bin                demo        gap-4.10.2.tar  public_html
CS_Comps_Parallel  gap-4.10.2  MegaSAS.log     __pycache__
(gap) [dhuth@enigma ~]$ cd CS_Comps_Parallel/
(gap) [dhuth@enigma CS_Comps_Parallel]$ git pull
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 6 (delta 3), reused 5 (delta 2), pack-reused 0
Unpacking objects: 100% (6/6), done.
From https://github.com/Danhuth/CS_Comps_Parallel
   f75174d..086197e  master     -> origin/master
Updating f75174d..086197e
error: Your local changes to 'ParallelGapCall.py' would be overwritten by merge.  Aborting.
Please, commit your changes or stash them before you can merge.
(gap) [dhuth@enigma CS_Comps_Parallel]$ exit
logout
Connection to enigma closed.
DanMac:~ dhuth$ cd Desktop/CS_Comps_Parallel/
DanMac:CS_Comps_Parallel dhuth$ ls
Output_Collator.py	ParallelGapCall.py	ParallelGenerator.py	parallelCall.py
DanMac:CS_Comps_Parallel dhuth$ git add all
fatal: pathspec 'all' did not match any files
DanMac:CS_Comps_Parallel dhuth$ git add -all
error: did you mean `--all` (with two dashes ?)
DanMac:CS_Comps_Parallel dhuth$ git add --all
DanMac:CS_Comps_Parallel dhuth$ git commit -m "retrying the commit without weird stuff"
[master 80c812e] retrying the commit without weird stuff
 2 files changed, 12 insertions(+), 11 deletions(-)
 create mode 100644 .DS_Store
DanMac:CS_Comps_Parallel dhuth$ git push
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 4 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 729 bytes | 364.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/Danhuth/CS_Comps_Parallel
   086197e..80c812e  master -> master
DanMac:CS_Comps_Parallel dhuth$ ssh enigma
dhuth@enigma's password: 
Last login: Thu Nov 14 11:33:08 2019 from 134.69.198.240

Your array seems to be healthy
[dhuth@enigma ~]$ workon gap
(gap) [dhuth@enigma ~]$ cd CS_Comps_Parallel/
(gap) [dhuth@enigma CS_Comps_Parallel]$ git pull
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 4 (delta 2), reused 4 (delta 2), pack-reused 0
Unpacking objects: 100% (4/4), done.
From https://github.com/Danhuth/CS_Comps_Parallel
   086197e..80c812e  master     -> origin/master
Updating f75174d..80c812e
error: Your local changes to 'ParallelGapCall.py' would be overwritten by merge.  Aborting.
Please, commit your changes or stash them before you can merge.
(gap) [dhuth@enigma CS_Comps_Parallel]$ git pull
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 4 (delta 3), reused 4 (delta 3), pack-reused 0
Unpacking objects: 100% (4/4), done.
From https://github.com/Danhuth/CS_Comps_Parallel
   80c812e..212675a  master     -> origin/master
Updating f75174d..212675a
error: Your local changes to 'ParallelGapCall.py' would be overwritten by merge.  Aborting.
Please, commit your changes or stash them before you can merge.
(gap) [dhuth@enigma CS_Comps_Parallel]$ git stash drop
No stash entries to drop
(gap) [dhuth@enigma CS_Comps_Parallel]$ git pull 
Updating f75174d..212675a
error: Your local changes to 'ParallelGapCall.py' would be overwritten by merge.  Aborting.
Please, commit your changes or stash them before you can merge.
(gap) [dhuth@enigma CS_Comps_Parallel]$ git stash

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: empty ident  <dhuth@enigma.oxy.edu> not allowed
Cannot save the current index state
(gap) [dhuth@enigma CS_Comps_Parallel]$ git config --global danhuth.email "danhuth@github.com"
(gap) [dhuth@enigma CS_Comps_Parallel]$ git config --global danhuth.name "Dan Huth"
(gap) [dhuth@enigma CS_Comps_Parallel]$ git stash 

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: empty ident  <dhuth@enigma.oxy.edu> not allowed
Cannot save the current index state
(gap) [dhuth@enigma CS_Comps_Parallel]$ git pull
Updating f75174d..212675a
error: Your local changes to 'ParallelGapCall.py' would be overwritten by merge.  Aborting.
Please, commit your changes or stash them before you can merge.
(gap) [dhuth@enigma CS_Comps_Parallel]$ git reset --hard
HEAD is now at f75174d Dumping parallel versions of program for testin
(gap) [dhuth@enigma CS_Comps_Parallel]$ git pull
Updating f75174d..212675a
Fast-forward
 .DS_Store            |  Bin 0 -> 6148 bytes
 ParallelGapCall.py   |   25 +++++++++++++------------
 ParallelGenerator.py |    4 +---
 parallelCall.py      |   15 +++++++++++++++
 4 files changed, 29 insertions(+), 15 deletions(-)
 create mode 100644 .DS_Store
 create mode 100644 parallelCall.py
(gap) [dhuth@enigma CS_Comps_Parallel]$ ls
Collated_Output.txt  Output_Collator.py  ParallelGapCall.py    __pycache__
genset               parallelCall.py     ParallelGenerator.py
(gap) [dhuth@enigma CS_Comps_Parallel]$ python3 ParallelGenerator.py 
Input a here: 2
input the number of bs you wish to find here: 10
Where would you like to store the generator sets? 
 Input here: genset
k for k*24 where k is the number of cores you have access to: 10
 Enter 1 to test the <a,b,kb, kb^2> case: 
 Enter 2 to test the <a^2, ab,b^2, S> 
 Enter 3 to test the <a^2, ab, b^2, ia^2 + jab + kb^2> with mod conditions case 
 Enter 4 to test the <a^3, a^2b,ab^2,b^3, S cubic term> case
 Here: 1
input K bound lower
 Here: 1
input K bound upper
 Here: 26
(gap) [dhuth@enigma CS_Comps_Parallel]$ ls
Collated_Output.txt        Generator_Storage_Folder3  Generator_Storage_Folder7  Output_Collator.py    __pycache__
Generator_Storage_Folder0  Generator_Storage_Folder4  Generator_Storage_Folder8  parallelCall.py
Generator_Storage_Folder1  Generator_Storage_Folder5  Generator_Storage_Folder9  ParallelGapCall.py
Generator_Storage_Folder2  Generator_Storage_Folder6  genset                     ParallelGenerator.py
(gap) [dhuth@enigma CS_Comps_Parallel]$ python3 parallelCall.py 
Traceback (most recent call last):
  File "parallelCall.py", line 13, in <module>
    pathTuple = (pathtuplecreator(),os.getcwd()+"/outputfile")
  File "parallelCall.py", line 10, in pathtuplecreator
    generator_storage_i = os.getcwd+"/Generator_Storage_Folder"+str(i)
TypeError: unsupported operand type(s) for +: 'builtin_function_or_method' and 'str'
(gap) [dhuth@enigma CS_Comps_Parallel]$ vim parallelCall.py 
(gap) [dhuth@enigma CS_Comps_Parallel]$ vim parallelCall.py 
(gap) [dhuth@enigma CS_Comps_Parallel]$ python3 parallelCall.py 
Traceback (most recent call last):
  File "parallelCall.py", line 15, in <module>
    sequencerun(GapCaller(pathTuple),pathTuple)
NameError: name 'sequencerun' is not defined
(gap) [dhuth@enigma CS_Comps_Parallel]$ cd
(gap) [dhuth@enigma ~]$ ls
bin  CS_Comps_Parallel  demo  gap-4.10.2  gap-4.10.2.tar  MegaSAS.log  public_html  __pycache__
(gap) [dhuth@enigma ~]$ cd demo
(gap) [dhuth@enigma demo]$ ls
demo.py  exit  outputs  __pycache__
(gap) [dhuth@enigma demo]$ vim demo.py
(gap) [dhuth@enigma demo]$ ls
demo.py  exit  outputs  __pycache__
(gap) [dhuth@enigma demo]$ cd
(gap) [dhuth@enigma ~]$ cd CS_
-bash: cd: CS_: No such file or directory
(gap) [dhuth@enigma ~]$ cd CS_Comps_Parallel/
(gap) [dhuth@enigma CS_Comps_Parallel]$ ls
Collated_Output.txt        Generator_Storage_Folder2  Generator_Storage_Folder5  Generator_Storage_Folder8  Output_Collator.py  ParallelGenerator.py
Generator_Storage_Folder0  Generator_Storage_Folder3  Generator_Storage_Folder6  Generator_Storage_Folder9  parallelCall.py     __pycache__
Generator_Storage_Folder1  Generator_Storage_Folder4  Generator_Storage_Folder7  genset                     ParallelGapCall.py
(gap) [dhuth@enigma CS_Comps_Parallel]$ vim parallelCall.py 
(gap) [dhuth@enigma CS_Comps_Parallel]$ python3 parallelCall.py 
Traceback (most recent call last):
  File "parallelCall.py", line 2, in <module>
    import clusterrun
ModuleNotFoundError: No module named 'clusterrun'
(gap) [dhuth@enigma CS_Comps_Parallel]$ cd
(gap) [dhuth@enigma ~]$ ls
bin  CS_Comps_Parallel  demo  gap-4.10.2  gap-4.10.2.tar  MegaSAS.log  public_html  __pycache__
(gap) [dhuth@enigma ~]$ cd demo
(gap) [dhuth@enigma demo]$ vim demo.py
(gap) [dhuth@enigma demo]$ cd
(gap) [dhuth@enigma ~]$ cd CS_Comps_Parallel/
(gap) [dhuth@enigma CS_Comps_Parallel]$ vim parallelCall.py 
(gap) [dhuth@enigma CS_Comps_Parallel]$ python3 parallelCall.py 
Traceback (most recent call last):
  File "parallelCall.py", line 2, in <module>
    from clusterrun import sequencerun
ModuleNotFoundError: No module named 'clusterrun'
(gap) [dhuth@enigma CS_Comps_Parallel]$ vim parallelCall.py 
(gap) [dhuth@enigma CS_Comps_Parallel]$ python3 parallelCall.py 
Traceback (most recent call last):
  File "parallelCall.py", line 16, in <module>
    sequencerun(GapCaller(pathTuple),pathTuple)
  File "/home/dhuth/CS_Comps_Parallel/ParallelGapCall.py", line 50, in GapCaller
    for filename in os.listdir(Generator_Set_File_Path):
FileNotFoundError: [Errno 2] No such file or directory: '<built-in function getcwd>/Generator_Storage_Folder0'
(gap) [dhuth@enigma CS_Comps_Parallel]$ ls
Collated_Output.txt        Generator_Storage_Folder2  Generator_Storage_Folder5  Generator_Storage_Folder8  Output_Collator.py  ParallelGapCall.py
Generator_Storage_Folder0  Generator_Storage_Folder3  Generator_Storage_Folder6  Generator_Storage_Folder9  outputfile          ParallelGenerator.py
Generator_Storage_Folder1  Generator_Storage_Folder4  Generator_Storage_Folder7  genset                     parallelCall.py     __pycache__
(gap) [dhuth@enigma CS_Comps_Parallel]$ packet_write_wait: Connection to 134.69.66.19 port 22: Broken pipe
DanMac:CS_Comps_Parallel dhuth$ 
  [Restored Nov 15, 2019 at 10:10:23 AM]
Last login: Fri Nov 15 10:10:13 on console
DanMac:CS_Comps_Parallel dhuth$ ls
Output_Collator.py	ParallelGapCall.py	ParallelGenerator.py	parallelCall.py
DanMac:CS_Comps_Parallel dhuth$ ssh enigma
dhuth@enigma's password: 
Connection closed by 134.69.66.19 port 22
DanMac:CS_Comps_Parallel dhuth$ ssh enigma
dhuth@enigma's password: 
Last login: Thu Nov 14 11:52:56 2019 from 134.69.198.240

Your array seems to be healthy
[dhuth@enigma ~]$ workon gap
(gap) [dhuth@enigma ~]$ ls
bin  CS_Comps_Parallel  demo  gap-4.10.2  gap-4.10.2.tar  MegaSAS.log  public_html  __pycache__
(gap) [dhuth@enigma ~]$ ls
bin  CS_Comps_Parallel  demo  gap-4.10.2  gap-4.10.2.tar  MegaSAS.log  public_html  __pycache__
(gap) [dhuth@enigma ~]$ cd CS_Comps_Parallel/
(gap) [dhuth@enigma CS_Comps_Parallel]$ ls
Collated_Output.txt        Generator_Storage_Folder2  Generator_Storage_Folder5  Generator_Storage_Folder8  Output_Collator.py  ParallelGapCall.py
Generator_Storage_Folder0  Generator_Storage_Folder3  Generator_Storage_Folder6  Generator_Storage_Folder9  outputfile          ParallelGenerator.py
Generator_Storage_Folder1  Generator_Storage_Folder4  Generator_Storage_Folder7  genset                     parallelCall.py     __pycache__
(gap) [dhuth@enigma CS_Comps_Parallel]$ python3 parallelCall.py 
Traceback (most recent call last):
  File "parallelCall.py", line 16, in <module>
    sequencerun(GapCaller(pathTuple),pathTuple)
  File "/home/dhuth/CS_Comps_Parallel/ParallelGapCall.py", line 50, in GapCaller
    for filename in os.listdir(Generator_Set_File_Path):
FileNotFoundError: [Errno 2] No such file or directory: '<built-in function getcwd>/Generator_Storage_Folder0'
(gap) [dhuth@enigma CS_Comps_Parallel]$ git
usage: git [--version] [--exec-path[=GIT_EXEC_PATH]] [--html-path]
           [-p|--paginate|--no-pager] [--no-replace-objects]
           [--bare] [--git-dir=GIT_DIR] [--work-tree=GIT_WORK_TREE]
           [--help] COMMAND [ARGS]

The most commonly used git commands are:
   add        Add file contents to the index
   bisect     Find by binary search the change that introduced a bug
   branch     List, create, or delete branches
   checkout   Checkout a branch or paths to the working tree
   clone      Clone a repository into a new directory
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   fetch      Download objects and refs from another repository
   grep       Print lines matching a pattern
   init       Create an empty git repository or reinitialize an existing one
   log        Show commit logs
   merge      Join two or more development histories together
   mv         Move or rename a file, a directory, or a symlink
   pull       Fetch from and merge with another repository or a local branch
   push       Update remote refs along with associated objects
   rebase     Forward-port local commits to the updated upstream head
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index
   show       Show various types of objects
   status     Show the working tree status
   tag        Create, list, delete or verify a tag object signed with GPG

See 'git help COMMAND' for more information on a specific command.
(gap) [dhuth@enigma CS_Comps_Parallel]$ git add parallelCall.py 
(gap) [dhuth@enigma CS_Comps_Parallel]$ git add parallelGapCall.py
fatal: pathspec 'parallelGapCall.py' did not match any files
(gap) [dhuth@enigma CS_Comps_Parallel]$ git add ParallelGapCall.py 
(gap) [dhuth@enigma CS_Comps_Parallel]$ git add ParallelGenerator.py 
(gap) [dhuth@enigma CS_Comps_Parallel]$ git commit -m "I don't really remember what I changed, it was definitely just some syntax stuff"
[master 2fe9ef2] I don't really remember what I changed, it was definitely just some syntax stuff
 Committer: dhuth <dhuth@enigma.oxy.edu>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

If the identity used for this commit is wrong, you can fix it with:

    git commit --amend --author='Your Name <you@example.com>'

 1 files changed, 3 insertions(+), 2 deletions(-)
(gap) [dhuth@enigma CS_Comps_Parallel]$ git commit --amend --author='Danhuth <dhuth@oxy.edu>' -m "I don't really remember what I changed, it was definitely just some syntax stuff"
[master 3988923] I don't really remember what I changed, it was definitely just some syntax stuff
 Author: Danhuth <dhuth@oxy.edu>
 Committer: dhuth <dhuth@enigma.oxy.edu>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

If the identity used for this commit is wrong, you can fix it with:

    git commit --amend --author='Your Name <you@example.com>'

 1 files changed, 3 insertions(+), 2 deletions(-)
(gap) [dhuth@enigma CS_Comps_Parallel]$ git commit --amend --author='Danhuth <dhuth@github.com>' -m "I don't really remember what I changed, it was definitely just some syntax stuff"
[master 18dd9cc] I don't really remember what I changed, it was definitely just some syntax stuff
 Author: Danhuth <dhuth@github.com>
 Committer: dhuth <dhuth@enigma.oxy.edu>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

If the identity used for this commit is wrong, you can fix it with:

    git commit --amend --author='Your Name <you@example.com>'

 1 files changed, 3 insertions(+), 2 deletions(-)
(gap) [dhuth@enigma CS_Comps_Parallel]$ git config --global user.name "Danhuth"
(gap) [dhuth@enigma CS_Comps_Parallel]$ git config --global user.email Dhuth@oxy.edu
(gap) [dhuth@enigma CS_Comps_Parallel]$ git commit --amend --author='Danhuth <dhuth@github.com>' -m "I don't really remember what I changed, it was definitely just some syntax stuff"
[master aec9fb3] I don't really remember what I changed, it was definitely just some syntax stuff
 Author: Danhuth <dhuth@github.com>
 1 files changed, 3 insertions(+), 2 deletions(-)
(gap) [dhuth@enigma CS_Comps_Parallel]$ git push
error: The requested URL returned error: 403 Forbidden while accessing https://github.com/Danhuth/CS_Comps_Parallel.git/info/refs

fatal: HTTP request failed
(gap) [dhuth@enigma CS_Comps_Parallel]$ git config --global user.email danhuth@github.com
(gap) [dhuth@enigma CS_Comps_Parallel]$ git commit --amend --author='Danhuth <dhuth@github.com>' -m "I don't really remember what I changed, it was definitely just some syntax stuff"
[master 90aa3e0] I don't really remember what I changed, it was definitely just some syntax stuff
 Author: Danhuth <dhuth@github.com>
 1 files changed, 3 insertions(+), 2 deletions(-)
(gap) [dhuth@enigma CS_Comps_Parallel]$ git push
error: The requested URL returned error: 403 Forbidden while accessing https://github.com/Danhuth/CS_Comps_Parallel.git/info/refs

fatal: HTTP request failed
(gap) [dhuth@enigma CS_Comps_Parallel]$ git config -l grep url
error: wrong number of arguments
usage: git config [options]

Config file location
    --global              use global config file
    --system              use system config file
    -f, --file <FILE>     use given config file

Action
    --get                 get value: name [value-regex]
    --get-all             get all values: key [value-regex]
    --get-regexp          get values for regexp: name-regex [value-regex]
    --replace-all         replace all matching variables: name value [value_regex]
    --add                 adds a new variable: name value
    --unset               removes a variable: name [value-regex]
    --unset-all           removes all matches: name [value-regex]
    --rename-section      rename section: old-name new-name
    --remove-section      remove a section: name
    -l, --list            list all
    -e, --edit            opens an editor
    --get-color <slot>    find the color configured: [default]
    --get-colorbool <slot>
                          find the color setting: [stdout-is-tty]

Type
    --bool                value is "true" or "false"
    --int                 value is decimal number
    --bool-or-int         value is --bool or --int
    --path                value is a path (file or directory name)

Other
    -z, --null            terminate values with NUL byte

(gap) [dhuth@enigma CS_Comps_Parallel]$ git config -L | grep url
error: unknown switch `L'
usage: git config [options]

Config file location
    --global              use global config file
    --system              use system config file
    -f, --file <FILE>     use given config file

Action
    --get                 get value: name [value-regex]
    --get-all             get all values: key [value-regex]
    --get-regexp          get values for regexp: name-regex [value-regex]
    --replace-all         replace all matching variables: name value [value_regex]
    --add                 adds a new variable: name value
    --unset               removes a variable: name [value-regex]
    --unset-all           removes all matches: name [value-regex]
    --rename-section      rename section: old-name new-name
    --remove-section      remove a section: name
    -l, --list            list all
    -e, --edit            opens an editor
    --get-color <slot>    find the color configured: [default]
    --get-colorbool <slot>
                          find the color setting: [stdout-is-tty]

Type
    --bool                value is "true" or "false"
    --int                 value is decimal number
    --bool-or-int         value is --bool or --int
    --path                value is a path (file or directory name)

Other
    -z, --null            terminate values with NUL byte

(gap) [dhuth@enigma CS_Comps_Parallel]$ git config -l |grep url
remote.origin.url=https://github.com/Danhuth/CS_Comps_Parallel.git
(gap) [dhuth@enigma CS_Comps_Parallel]$ git remote set-url origin "https://Danhuth@github.com/DanHuth/CS_Comps_Parallel.git"
(gap) [dhuth@enigma CS_Comps_Parallel]$ git config -l |grep url
remote.origin.url=https://Danhuth@github.com/DanHuth/CS_Comps_Parallel.git
(gap) [dhuth@enigma CS_Comps_Parallel]$ git push

(gnome-ssh-askpass:12836): Gtk-WARNING **: cannot open display: 
(gap) [dhuth@enigma CS_Comps_Parallel]$ unset SSH_ASKPASS
(gap) [dhuth@enigma CS_Comps_Parallel]$ git push
Password: 
error: The requested URL returned error: 403 Forbidden while accessing https://Danhuth@github.com/DanHuth/CS_Comps_Parallel.git/info/refs

fatal: HTTP request failed
(gap) [dhuth@enigma CS_Comps_Parallel]$ ls
Collated_Output.txt        Generator_Storage_Folder2  Generator_Storage_Folder5  Generator_Storage_Folder8  Output_Collator.py  ParallelGapCall.py
Generator_Storage_Folder0  Generator_Storage_Folder3  Generator_Storage_Folder6  Generator_Storage_Folder9  outputfile          ParallelGenerator.py
Generator_Storage_Folder1  Generator_Storage_Folder4  Generator_Storage_Folder7  genset                     parallelCall.py     __pycache__
(gap) [dhuth@enigma CS_Comps_Parallel]$ vim ParallelGapCall.py 
(gap) [dhuth@enigma CS_Comps_Parallel]$ vim ParallelGenerator.py 
(gap) [dhuth@enigma CS_Comps_Parallel]$ vim ParallelGapCall.py 
(gap) [dhuth@enigma CS_Comps_Parallel]$ vim ParallelGenerator.py 

        X2_List = range(Lower_Bound_Of_X2, Upper_Bound_Of_X2)
        AllGenSets = []
        for i in range(0, len(List_Of_A_Relative_Primes)):
            for j in range(0, len(X0_List)):
                for k in range(0,len(X1_List)):
                    for l in range(0,len(X2_List)):
                        if X0_List[j] <= List_Of_A_Relative_Primes[i] & X1_List[k]<= List_Of_A_Relative_Primes[i]:
                            Sterm = X0_List[j]*Base_A_Value**2 + X1_List[k]*Base_A_Value*List_Of_A_Relative_Primes[i] + X2_List[l]*List_Of_A_Relative_Primes[i]**2
                            if(Sterm % (List_Of_A_Relative_Primes[i]-Base_A_Value) == Base_A_Value**2 % (List_Of_A_Relative_Primes[i]-Base_A_Value) or  Sterm % (List_Of_A_Relative_Primes[i] + Base_A_Value) == Base_A_Value**2 % (List_Of_A_Relative_Primes[i] + Base_A_Value)):
                                AllGenSets.append((Base_A_Value**2, Base_A_Value*List_Of_A_Relative_Primes[i], List_Of_A_Relative_Primes[i]**2, Sterm))
        SetsToTest = AllGenSets
        for i in range(len(SetsToTest)):
            iteratorstring = str(i)
            file = open(Generator_Set_File_Path+Generator_Set_Filename+iteratorstring+'.g','w')
            S = Format_For_Gap(SetsToTest[i])
            file.write(S)

    if(Generator_Style_Case == 4):
        file = open(Generator_Set_Filename,'w')
        lowerL = int(input('input L bound lower\n Here:'))
        upperL = int(input('input L bound upper\n Here:'))
        X0_List = range(0,b)
        X1_List = range(0,b)
        X2_List = range(0,b)
        X3_List = random.sample(range(lowerL, upperL), (upperL-lowerL)-1)
        Number_Of_Gen_Sets_To_Generate = 24*int(input('k for k*24 where k is the number of cores you have access 2'))
        AllGenSets = []
        for i in range(0, len(List_Of_A_Relative_Primes)):
            for j in range(0, len(X0_List)):
                for k in range(0,len(X1_List)):
                    for l in range(0,len(X2_List)):
                        for m in range(0,len(X3_List)):
                            if(X0_List[j] <= List_Of_A_Relative_Primes[i] & X1_List[k] <= List_Of_A_Relative_Primes[i] & X2_List[l] <= List_Of_A_Relative_Primes[i]):
                                Sterm = X0_List[j]*Base_A_Value**3 + X1_List[k]*Base_A_Value**2*List_Of_A_Relative_Primes[i] + X2_List[l]*Base_A_Value*List_Of_A_Relative_Primes[i]**2 + X3_List[m]*List_Of_A_Relative_Primes[i]**3
                                if(Sterm % List_Of_A_Relative_Primes[i]-Base_A_Value == 0):
                                    AllGenSets.append((Base_A_Value**3, Base_A_Value**2*List_Of_A_Relative_Primes[i], Base_A_Value*List_Of_A_Relative_Primes[i]**2,List_Of_A_Relative_Primes[i]**3,Sterm))
        SetsToTest = random.sample(AllGenSets,Number_Of_Gen_Sets_To_Generate)
        for i in range(Number_Of_Gen_Sets_To_Generate):
            iteratorstring = str(i)
            file = open(Generator_Set_File_Path+corenumber+Generator_Set_Filename+iteratorstring+'.g','w')
            S = Format_For_Gap(SetsToTest[i])
            file.write(S)

#Cleaning_Script(Generator_Set_File_Path)
Generator_Set_Generator(Base_A_Value, Num_Relative_Primes)
