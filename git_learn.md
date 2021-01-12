# Git教程
## 1.安装Git
1.在Windows上下载安装Git  
2.运行Git.bash软件  
3.输入用户名和邮箱  
+ git config --global user.name #输入用户名  
+ git config --global user.email #输入邮箱  

## 2.操作
### 2.1创建本地版本库

### 2.2本地仓库操作
#### 2.2.1 基础操作
1.查看状态<br>
 - git status 

2.撤销对文件的修改，在add之前<br>
 - git restore file 
   
3.删除文件<br>
 - git rm file

4.管理修改（Git跟踪的是修改，而不是文件）
 - git add file #添加文件到缓存区<br>
 - git commit -m "对文件操作的描述" # 将文件提交到仓库，这一步之后，无法撤销修改，只能回退<br>
 
5.版本回退
 - HEAD #指针，指向当前版本号；
 - git log --pretty=oneline  #查看提交历史
 - git reflog  #查看命令历史
 - git reset --hard commit_id #回退版本


