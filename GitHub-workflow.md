# Contributing to the existing repository
# download a repository on GitHub to our machine
git clone git@github.com:Kenzie5/act-practice.git

# create a new branch to store any new changes
git branch my-branch

# switch to that branch (line of development)
git checkout my-branch

# make changes, for example, edit `file1.md` and `file2.md` using the text editor

# stage the changed files
git add file1.md file2.md

# or add all with -A
git add -A

# take a snapshot of the staging area (anything that's been added)
git commit -m "desc of what was changed"

# push changes to github
git push --set-upstream origin my-branch
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Contributing to an existing branch on GitHub

# update all remote tracking branches, and the currently checked out branch
git pull

# change into the existing branch called `feature-a`
git checkout feature-a

# make changes, for example, edit `file1.md` using the text editor

# stage the changed file
git add file1.md

# take a snapshot of the staging area
git commit -m "edit file1"

# push changes to github
git push
