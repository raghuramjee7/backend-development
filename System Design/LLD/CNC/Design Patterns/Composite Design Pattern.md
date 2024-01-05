# Composite Pattern

1. Composite pattern deals with object inside object
2. Whenever a problem has a tree structure, we can use composite pattern
3. The problem composite pattern is trying to solve is - when we have a tree like struture of subobjects and we dont know which object is at which level, we need to use if else blocks everytime to check which object is at which level, and then perform the operation on that object. This is not a good design, and we can use composite pattern to solve this problem.
4. This issue happens because the list of subobjects is not fixed, and we dont know how many subobjects are there, and we dont know which object is at which level. So we generically use Object class to store all the subobjects, and then we need to check which object is at which level, and then perform the operation on that object.

## Implementation
1. We have a file system, which has files and folders, and folders can have files and folders inside them.
2. We have a file system interface, with an ls() method.
3. We then create concrete classes that implement this interface, and we have a file class and a folder class.
4. Now, the list of subobjects is of type FileSystem, so we can store both files and folders in this list and we can call the ls method without knowing which object is at which level.