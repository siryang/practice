# Comand of Git


`git push <remote_repo> <local_branch>:<remote_branch>`

`git reset` remove change in file.

`git revert` remove commit.

`git clean -d` remove untracked files from the working tree.

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