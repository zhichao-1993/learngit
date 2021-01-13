# Git教程
## 1.安装Git
1.在Windows上下载安装Git  
2.运行Git.bash软件  
3.输入用户名和邮箱  
+ git config --global user.name #输入用户名  
+ git config --global user.email #输入邮箱  
---
## 2.操作

### 2.1创建本地版本库
#### 2.1.1从头创建版本库（两步）
##### 1.创建空目录  
 - mkdir learngit 创建空目录  
 - cd learngit 进入空目录  
 - pwd  查看当前所在位置  
 
##### 2. git init  将空目录变成Git的仓库，生成一个.git隐藏文件  。

#### 2.1.2从GitHub上克隆一个版本库
##### 1. git clone remote_repo_addr 从远程仓库clone到本地

 ---
### 2.2本地仓库操作
#### 2.2.1 基础操作
##### 1.查看状态<br>
 - git status 

##### 2.撤销对文件的修改，在add之前<br>
 - git restore file 
   
##### 3.删除文件<br>
 - git rm file

##### 4.管理修改（Git跟踪的是修改，而不是文件）
 - git add file #添加文件到缓存区<br>
 - git commit -m "对文件操作的描述" # 将文件提交到仓库，这一步之后，无法撤销修改，只能回退<br>
 
##### 5.版本回退
 - HEAD #指针，指向当前版本号；
 - git log --pretty=oneline  #查看提交历史
 - git reflog  #查看命令历史
 - git reset --hard commit_id #回退版本

#### 2.2.2分支操作
##### 1.查看分支  
 - git branch -a  查看本地远程所有的分支  
 - git branch -r  查看所有远程分支  
 
##### 2.创建新的分支    
 - git branch new_branch_name 
    
##### 3.删除分支  
 - git branch -d branch_name  退出所要删除的分支，切换到其他分支，才可以删除  

##### 4.切换分支  
 - git checkout branch_name  

##### 5.新建并切换到此分支，切换和新建两个命令合二为一  
 - git checkout -b new _branch_name  

##### 6.合并temp到当前分支
 - git merge temp  

##### 7.获取主机origin的master分支的更新,到本地分支temp上
 - git fetch origin master:temp
 
####2.2.3远程仓库操作
##### 1.git clone(远程仓库-->本地仓库)
 1. git clone <版本库网址> 从远程仓库clone到本地
 2. git clone <版本库网址> <本地目录名> 从远程仓库clone到本地指定文件夹（远程仓库的名字不是你想要的）  
 3. 使用镜像clone远程仓库（在github.com后面加cnpmjs.org）  
   - git clone https://github.com/zhichao-1993/learngit.git  
   - git clone https://github.com.cnpmjs.org/zhichao-1993/learngit.git  

##### 2.git remote   
  1. git remote   显示主机名   
  2. git remote -v  显示所有的主机名  
  3. git clone -o <版本库网址> 克隆的同时，修改主机名  
  4. git remote show <主机名> 查看主机的所有详细信息  
  5. git remote add <主机名> 添加远程主机  
  6. git remote rm <主机名> 删除远程主机  
  7. git remote rename <旧主机名><新主机名> 修改远程主机名  
 
##### 3.git fetch(远程仓库-->本地仓库)
  1. git fetch <主机名 origin> 将主机上的更新，全部取回本地  
  2. git fetch <主机名  origin>< 指定分支名  master> 取回指定分支上的更新  
  3. git checkout -b newBranch origin/master 将master分支的更新取回本地，放到新创建的newBranch分支上，并切换到此分支  
  4. git fetch origin master:temp  将master分支的更新取回，放到本地的temp分支上  
  5. git merge origin/master 在本地分支合并远程分支  
  
##### 4.git pull(远程仓库-->工作区)  
   1. git pull origin next:master  取回远程主机的分支origin/next取回本地，与本地分支master进行合并  
      + git pull <远程主机名><远程分支名>:<本地分支名>
      + 相当于以下两步操作
      + git fetch origin  远程分支先取回本地  
      + git merge origin/next  在进行合并  
   2. git branch --set-upstream master origin/next
      + git branch --set-upstream <本地分支> <远程主机名>/<远程分支名>
      + 当本地分支与远程分支没有进行追踪关系时，即可进行以上操作
      + 将本地master分支与远程的next分支建立追踪关系
   3. git pull origin
      + 将本地分支与远程主机上建立“追踪关系的分支”进行合并
   4. git pull -p
      + 本地删除远程已经删除的分支  

##### 5.git push(本地分支更新，推送到远程主机)
   1. git push origin master
      + git push <远程主机名><本地分支名>:<远程分支名>
      + 省略远程分支名，把本地分支推送到与它建立追踪关系的远程分支上
   2. git push origin :master
      + 省略本地分支名，将会删除指定的远程分支，等同与推送了一个空的本地分支到远程分支上
   3. git push origin
      + 本地分支与远程分支建立追踪关系，本地分支名与远程分支名可以省略
   4. git push 
      + 如果当前分支只有一个追踪分支，所有都可以省略
   5. git push -u origin master
      + 如果当前分支与多个主机存在追踪关系，使用-u指定一个默认主机
   6. git push --all origin
      + 将本地的所有分支推送到远程主机

## 3.感悟
 1.对分支的感悟  
   + 在master分支的基础上，可以建立相对于它的分支
   + 在master分支的分支的基础上，可以建立相对于它的分支
 
 2.手动建立本地分支与远程分支的追踪关系
   + 远程上没有建立分支
        + git push --set-upstream origin branch_loc_name #推送本地分支到远程并建立跟踪，远程如果没有，就创建此分支
   + 远程上建立了分支，但是没有追踪
        +  手动建立追踪关系 git branch --set-upstream=origin/a a 
            + git branch --set-upstream-to=<远程主机名>/<远程分支名> <本地分支名>  
        +  push时建立追踪关系 git push -u origin b 
            + git push -u <远程主机名><本地分支名>
            + 本地分支和远程分支同名的分支进行追踪
        +  新建分支的时候建立追踪 git checkout -b c origin/c
            + git checkout -b <新建的本地分支名> <远程主机名>/<远程分支名>