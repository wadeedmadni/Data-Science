# Day 0 - Learning Python & Data Science from Scratch
# Learning Git basics

1. Install git to your local machine for [Windows](https://gitforwindows.org/)
2. Make a folder in your local machine with any name
3. Opem CMD (command prompt) and access the folder which you have just made.
  - You can use 
  ``` 
  cd <path_to_your_folder>
  ```
4. Initialize git repository
```
git init
```
5. Check status of your files if there are any changes made
```
git status
```
6. Now add Changes to the state changes
```
#You can add changes in your file one by one
git add <path_to your_file>

#You can add changes made in all files all at once
git add .
```
7. Commit the changes
```
git commit -m "<add a useful message for your ownself to mark what changes you have made in this file or version number>"
```
8. Sync the changes made ```
git push
```
9. You can use Visual Code for this as well, you need to login from your github account.