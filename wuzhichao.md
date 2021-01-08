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

## 3.添加文件到版本库
    git add "文件名"  (将文件添加到git）
    git commit -m "对文件操作的说明"  （把文件提交到仓库）
    