## Introduction

## Example

## Something

## Login


## Chat

## initialize a new Git local repo
git init
## check the current state of your project
## you can always type this to check your change
git status
## stage a specific file
git add <filename>
## stage all untracked and modified files
git aff
# comment staged changes to the repo
git commit -m "your commit message"
# show the detailed history of all commits
git log
# displau a one-line summary of each commit
git log --oneline
# switch to <branch-name> branch
git switch <branch-name>
# merge 2 branches
# Remember witch to the branch you want to merge into (e.g.main) before running the merge command
git merge <branch-name>
## delete <branch-name>
git branch -D <branch-name>
# store your changes
git stash
# apply changes & delete stashed changes
git stash pop
# without record
git reset <targer-hash> 
# with a revert record
git revert <target-hash>

## no needed