# 1. Version Control using Git

Version control allows you to save your code base at different steps and revert back to a previous version if something went horribly wrong.

# You initialize a local Git repo with command:
git init

# You add files to be tracked to the Staging Area with: 
git add

# You can check the status of the Staging Area with:
git status

# To commit changes from the Staging area we use the command:
git commit -m  
# -m is the option to add a Commit Message
# By convention, commit message should be in present tense and to add as much detail of what was changed from the previous commit

# To see what commits you have made, you use:
git log
# each commit has a unique hash by which it is identified
# the HEAD shows at which position we are

# In case of a mistake, we can revert back to the last commit in the Git repo by using:
git checkout <filename>

# Before we revert the changes, we can check the differences between last commit and the local files with:
git diff <filename>


# 2. Git Remote Repositories using GitHub

# After you create a GitHub free account, you can create a remote repository.
# By default, all repositories are Public, but can be changed to Private.

# Following the instructions on GitHub, you can push an existing local repo to the newly created GitHub repo
git remote add origin <url>
# <origin> - name of local repo (it can be anything but by convention, most developers use origin)
# <url> - the URL of the remote repo on GitHub

git push -u origin main
# -u - links the remote and local repository
# <origin> - name of the remote repo
# <main> - branch to be pushed to (main is the default branch for any new repos)


# 3. Git Main Branch

- the sequence of commits is the Main Branch of your Repository
- you can keep track of different commits locally from the remote repository in GitHub
- until you <push> the changes, all commits will be tracked by the local git repo in the folder <.git>


# 4. How to use <.gitignore>

# You can set rules to prevent committing certain files to the remote repo using the <.gitignore> file
# Especially useful to prevent sending to the internet files that contain API keys, Secrets, environments settings etc.

# The file has to be created, it is not created by default by Git.
# Each file name to be ignored is added on a separate line

# <.gitignore> has certain syntax rules:
- # to add a comment
- it accepts <wildcards> like * to ignore all files with a certain extension like <*.log>


# 5. Git Clone - how to download and create a copy of a repository

git clone <url>
# Pulls down all the files, commits and history of a remote repository and creates a local copy of it in a local repository

# Fun repos to clone and mess around with
https://github.com/ritik48/Wordle-Game


# 6. Branching and Merging - How to use branches to develop features and to collaborate on a codebase.

# Feature development with branches
git branch name-of-branch

# Main      1   -->    2     -->      3     >  4    -->     5
# Feature 1              \>   3   -->    4 /

git merge name-of-branch
# will bring all the changes and commits from the experimental branch into the Main Branch

git branch
# Will show all the branches in your git repo
# the * shows which branch you are currently on

# To switch to another branch you use:
git checkout name-of-branch

# You then develop the features and commit to the new branch
# WHen ready to merge with the main branch, you do :
git checkout main
git merge name-of-branch
# This will also add the history of all commits from the other branch
# To merge in a single commit without the history, you use:
git merge --no-ff name-of-branch
# --no-ff stands for no fast-forward


# 7. Forking and Pull Requests - How to suggest code changes and contribute to open-source projects

# Making a copy of a remote repository that you do not own is called Forking.
# This will make a copy in your own GitHub account that you fully control and can change.

# All public repositories have <read-only> access for anyone that forks it.
# On large projects, there is usually a team of people that have Collaborator status and all have <write> access to the same repo.

# For other people, to request changes to the owner of the repo, they need to raise a <Pull Request>
# The owner then reviews the changes and can <Approve> the Pull Request which will merge the changes into the repo.



