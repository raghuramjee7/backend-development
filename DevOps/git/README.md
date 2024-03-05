# Git

1. Git uses checksums to track changes. It uses SHA-1 algorithm to generate a 40-character checksum, we use the first 7 characters to identify a commit.
2. Make change -> add it to staging area -> commit it to local repository -> push it to remote repository.

## Commands
1. `git add .` - Add all files to staging area
2. `git commit -m "message"` - Commit changes to local repository
3. `git push` - Push changes to remote repository
4. `git pull` - Pull changes from remote repository
5. `git status` - Check status of files
6. `git log` - Check commit history
7. `git branch` - Check branches
8. `git checkout -b branch_name` - Create a new branch
9. `git checkout branch_name` - Switch to a branch
10. `git merge branch_name` - Merge a branch
11. `git branch -d branch_name` - Delete a branch
12. `git clone url` - Clone a repository
13. `git remote -v` - Check remote repository
14. `git remote add origin url` - Add remote repository
15. `git remote remove origin` - Remove remote repository
16. `git push origin --delete branch_name` - Delete a remote branch
17. `git config --global user.name "name"` - Set username
18. `git config --global user.email "email"` - Set email
19. `git config --global --list` - Check global configuration
20. `git init -b default_branch_name` - Initialize a new repository
21. `git reset --hard` - Reset to last commit
22. `git reset --hard commit_id` - Reset to a specific commit
23. `git reset --soft commit_id` - Reset to a specific commit and keep changes
24. `git reset HEAD file_name` - Unstage a file
25. `git checkout -- file_name` - Discard changes in working directory
26. `git clean -f` - Remove untracked files
27. `git clean -f -d` - Remove untracked directories
28. `git stash` - Stash changes
29. `git stash list` - List stashes
30. `git stash apply` - Apply last stash
31. `git stash apply stash_id` - Apply a specific stash
32. `git stash drop` - Drop last stash
33. `git stash drop stash_id` - Drop a specific stash
34. `git stash pop` - Apply and drop last stash
35. `git commit -a -m "message"` - Add and commit changes
36. `git commit --amend -m "message"` - Amend last commit
37. `git rebase branch_name` - Rebase a branch
38. `git diff branch_name` - Check changes that happened
39. `git diff --staged` - Check changes in staging area
40. `git rm --cached file_name` - Remove file from staging area
41. `git tag` - Check tags
42. `git tag -a tag_name -m "message"` - Create a tag. There are two types of tags, annotated and lightweight. Annotated tags are stored as full objects in the Git database. They’re checksummed; contain the tagger name, email, and date; have a tagging message; and can be signed and verified with GNU Privacy Guard (GPG). Lightweight tags are just a pointer to a specific commit. We create a tag after a commit.
43. `git tag -d tag_name` - Delete a tag
44. `git push origin tag_name` - Push a tag
45. `git show tag_name` - Show tag details
46. `git push origin --tags` - Push all tags
47. `git log --pretty=oneline` - Check commit history in one line
48. `git log --graph --oneline --all` - Check commit history in graph