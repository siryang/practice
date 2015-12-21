# Comand of Git


`git push <remote_repo> <local_branch>:<remote_branch>`

`git reset` remove change in file.

`git revert` remove commit.

`git clean -d` remove untracked files from the working tree.

`git push origin :remote_branch` delete remote branch.

`git add -u`: rm all deleted file.

```
自动补全脚本
wget https://raw.github.com/git/git/master/contrib/completion/git-completion.bash --no-check-certificate
mv git-completion.bash ~/.git-completion.bash

在~/.bash_profile中添加：
if [ -f ~/.git-completion.bash ]; then
    . ~/.git-completion.bash
fi
```

# SSH for Git

``` shell
ssh-keygen -t rsa -C "your_email@domain.com"
pbcopy < ./id_rsa.pub

ssh-add ~/.ssh/id_rsa
ssh-agent bash
ssh -T git@domain.com

```

# 设置

colorful git:  `git config --global color.ui auto`


# 修改历史

``` 修改最后一次提交
git reset HEAD^
git add
git commit -m “MSG”
```

改最后一次提交的作者
`git commit –amend –author=<user-email>`


```
#修改没有push过的版本
git filter-branch -f --commit-filter '
        if [ "$GIT_AUTHOR_EMAIL" = "the old email" ];
       then
                GIT_AUTHOR_NAME="your name";
                GIT_AUTHOR_EMAIL="your new email";
                git commit-tree "$@";
        else
                git commit-tree "$@";
        fi' -- 你的版本^..HEAD HEAD
```

```
#修改你当前分支的所有版本，包括已经push过的
git filter-branch -f --commit-filter '
        if [ "$GIT_AUTHOR_EMAIL" = "the old email" ];
       then
                GIT_AUTHOR_NAME="your name";
                GIT_AUTHOR_EMAIL="your new email";
                git commit-tree "$@";
        else
                git commit-tree "$@";
        fi' HEAD
```
