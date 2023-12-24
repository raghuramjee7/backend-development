# Linux Commands

1. `ls` - list files and directories, `-a` - list all files and directories, including hidden files and directories, `-l` - list files and directories in long format, `-la` - list all files and directories in long format, including hidden files and directories, `-r` to print in recursively
2. `mkdir <folder_name>` - create a directory
3. `cd <folder_name>` - change directory, `..` - go back one directory, `~` - go to home directory, `-` - go to previous directory
4. `pwd` - print working directory
5. `touch <file_name>` - create a file
6. `cat <file_name>` - print the contents of a file, `cat <file1> <file2> > <file3>` - concatenate two files and store the result in a third file
7. `open <path>` - open a file or folder
8. `cp <source> <destination>` - copy a file or folder
9. `mv <source> <destination>` - move a file or folder
10. `rm <file_name>` - remove a file
11. `rm -rf <folder_name>` - remove a folder
12. `clear` - clear the terminal
13. `where <command>` - find the location of a command
14. `echo $PATH` - print the path variable, each path variable is seperated by a colon, each time we run a command, the computer checks in all the paths in the path variable to find the command, if a command is found, it is run, else it is not run
15. `export PATH=$PATH:<path>` - add a path to the path variable
16. `nano <file_name>` - open a file in nano editor
17. `man <command>` - open the manual for a command
18. `history` - print the history of commands
19. `mkdir <folder_name>` - create a directory and all its parent directories, `mkdir -p <folder_name>` - create a directory and all its parent directories
20. `rmdir <folder_name>` - remove a directory, `rmdir -p <folder_name>` - remove a directory and all its parent directories
21. `rm -i <file_name>` - remove a file and ask for confirmation, `rm -rf <file_name>` - remove a file without asking for confirmation.
22. `sudo <command>` - run a command as root user, stands for super user do
23. `df` - print the disk usage of the file system, `-h` - print the disk usage of the file system in human readable format. `du` - print the disk usage statistics.
24. `head <file_name>` - print the first 10 lines of a file, `head -n <number_of_lines> <file_name>` - print the first n lines of a file, `tail <file_name>` - print the last 10 lines of a file, `tail -n <number_of_lines> <file_name>` - print the last n lines of a file
25. `diff <file1> <file2>` - compare two files line by line, `diff -y <file1> <file2>` - compare two files line by line and print the output side by side
26. `locate <file_name>` - find a file, `locate -i <file_name>` - find a file case insensitively, `locate -c <file_name>` - find the number of files found, `locate -S` - find the size of the database
27. `find <path> -name <file_name>` - find a file in a directory, `find <path> -name <file_name> -type f` - find a file in a directory, `find <path> -name <file_name> -type d`
28. `chmod <permission> <file_name>` - change the permissions of a file, `u=rwx,g=rx,o=r` here the permission given is user can read, write, excute. group can read, excute. others can read. `777` permission means all can read, write, excute. First digit is user, second digit is group, third digit is others. 4 stands for read, 2 stands for write, 1 stands for excute, 0 for no permission. So the sum of 4,2,1 is 7 for rwx.
29. `chown <user_name> <file_name>` - change the owner of a file.
30. `find . -type f -name "*.txt* -exec em -rf {} +` - for all the objects in the current directory of type file and name ending with .txt, remove the file. Here {} is the placeholder and + for all the files, each file name is concatenated.
31. `grep <pattern> <file_name>` - search for a pattern in a file. grep stands for global regular expression print. There are many flags for this similar to find command
32. `wget <url>` - download a file from the internet
33. `top` - display the processes running and the resources they are using.
34. `kill <process_id>` - kill a process
35. `uname` - print the name of the operating system, `uname -a` - print all the information about the operating system
36. `zip <zip_name> <file1> <file2>` - zip files, `unzip <zip_name>` - unzip files
37. `useradd <user_name>` - add a user, `userdel <user_name>` - delete a user, `passwd <user_name>` - change the password of a user
38. `lscpu` - print the cpu information
39. `nslookup` - print the dns information

## Operators
1. & - Command is run in the background
2. && - Run the second command only if the previous command is successful
3. Use ; to seperate multiple commands
4. Use || to run the second command only if the previous command fails
5. Use | to send the output of one command to another command
6. !() use not command to negate the output of a command
7. Use > to override the output of a command to a file, >> to append
8. We can put a bunch of commands in {} to group a set of commands, eg - if first command runs, then run these bunch of commands.

