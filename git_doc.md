# Git 常用操作 

## 1 安装
### 1.1 window 安装
    下载 Git for Windows 
    在命令行设置用户名和密码（用来分辨修改提交者,需要替换成自己的名字和邮箱地址）：
       git config --global user.name "Your Name"
       git config --global user.email "email@example.com"
    若需要连接远程仓库需要生成公钥和私钥,并把公钥放到远程仓库
       ssh-keygen -r rsa -C "email@exampple.com" 
   
## 2 操作
### 2.1 创建一个本地仓库：
        mkdir myrepo  && git init  # 本地新建一个空文件夹并初始化为仓库
        git clone  remote_repo_adds  # 从远程clone一个远程仓库
        创建远程仓库后,会在文件夹myrepo内部有一个.git 的隐藏文件夹，后面的一切git 命令执行都需要先进入cd到仓库内
        即 cd myrepo 后才可以执行下面的命令
### 2.2 本地仓库：
#### 2.2.1 修改提交，撤回，版本回退
        git status
        git restore file  # 撤销对文件的修改，before add
        git add file  # 撤销 git restore --staged file
        git commit -m "you commit of this" # 到此无法撤回,只能回退
        git reset --hard commit-id # 回退版本
#### 2.2.2 分支操作,查看，创建，切换,合并
        git branch [-a] # 查看当前的所在分支，加 -a 会显示所有的分支 [-r] 远程仓库
        git branch  new_branch_name  # 新建分支
        git branch -d new_branch_name # 删除分支
        git checkout branch_name
        git checkout -b new_branch_name # 新建并切换到此分支,相当于前两条命令组合
        git fetch origin master:temp  # 获取远程master分支到本地temp 分支
        git merge temp    # 合并 temp 到当前分支

### 2.3 远程仓库
        git clone git@github.com:Username/Reponame.git 后远程主机名默认为origin
        git remote show <主机名>        # 查看远程主机
        git remote add <主机名> <网址>   # 添加远程主机
        git remote rm <主机名>          # 删除
        git remote rename <原主机名> <新主机名>  # 重命名  
        git remotes [-v] # 查看关联的远程仓库,加 -v 会显示详细信息
        git push      # 本地推送到远程仓库
        


    

