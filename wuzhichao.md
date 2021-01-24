# Git分布式版本控制系统

## 1.安装Git
### 1.启动Git Bash    (输入两个参数)

    git config --global user.name
    
    git config --global user.email

## 2.创建版本库
    
	~mkdir~ learngit  #创建空目录
    cd learngit
    pwd
    
    git init #将目录变成git可以管理的仓库
    git clone #将远程仓库拷贝到本地
    git clone remote_repo_addr signin  #clone远程仓库到本地指定文件夹signin 
    使用镜像克隆（在github.com后面添加cnpmjs.org）
    git clone https://github.com/Hackergeek/architecture-samples
    git clone https://github.com.cnpmjs.org/Hackergeek/architecture-samples
    
## 3.添加文件到版本库
    git add "文件名"  (将文件添加到git）
    git commit -m "对文件操作的说明"  （把文件提交到仓库）
    
## 4.远程仓库操作
    git push #本地推送到远程 
    git pull #获取远程仓库的更新到本地
    
## 5.本地分支操作
    git branch dev #创建一个叫dev分支
    git branch -d dev #删除dev分支
    git checkout dev #切换到dev分支
    git checkout -b dev #新建dev并切换到此分支
    git branch -a #查看所有分支
    git merge dev #合并dev到当前分支
    git push --set-upstream origin branch_loc_name #推送本地分支到远程并建立跟踪，远程如果没有，就创建此分支
    
## 6.


