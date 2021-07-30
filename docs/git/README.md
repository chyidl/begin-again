# Git Tips

## Table of Contents
* [How To Add and Update Git Submodules](#submodule)

submodule
---------
> Git submodules are most of the time used in order to incorporate another versioned project within an existing project.

# Optionally, you can specify target directory (it will be included in a directory named as the remote repository name if not provided)
$ git submodule add <remote_url> <destination_folder>

# commit submodule by using the "git commit"
$ git commit -m "Added the submodule to the project."
$ git push

# When adding a new Git submodule into your peoject, multiple actions will be performed for you:
    1. A folder is created in your Git repository named after the submodule that you chose to add
    2. A hidden file name ".gitmodules" is created in your Git repository: this file contains the references to the remote repositories that you cloned as submodules.
    3. Git configuration (located at .git/config) was also modified in order to include the submodule you just added.
    4. The submodule you just added are marked as changes to be committed in your repository.

# Pull a Git Submodule
> Whenever you are cloning a Git repository having submodules, you need to execute an extra command in order for the submodules to be pulled.
> If you don't execute this command, you will fetch the submodule folder, but you won't have any content in it.
$ git submodule update --init --recursive

# Update a Git Submodule
> In order to update an existing Git submodule, you need to execute the "git submodule update" with the "-remote" and the "-merge" option.
> Using this command, your detached HEAD will be updated to the newest commit in the submodule repository.
$ git submodule update --remote --merge

# Fetch new submodule commits
$ cd repository/submodule
$ git fetch (you will get the new submodule commits)
> see the new commit
$ git log --oneline origin/master -3

begin-again on  main
➜ git checkout -q 6dc316f

# Remove Git submodules
> In order to remove a Git submodule from your repository, use the "git submodule deinit" command followed by the "git rm" command and specify the name of the submodule folder


$ git submodule deinit <submodule>  # delete the local submodule configuration stored in your repository (.git/config will be delete)
$ git rm <submodule> # delete submodules files from the working directory and remaining .git folders.

# Configuring submodules for your repository
> hava a submodule summary when executing "git status"
$ git config --global status.sumoduleSummary trueA
> git diff command to have detailed information about your submodule, use the "git config" command with the diff.submodule parameter set to true.
$ git config --global diff.submodule log
```
