#  Git在Pycharm的使用教程
## 1. 在本地建立新仓库 git init   
## 2. 新电脑需要配置SSH    
  + 配置用户名 git config --global user.name'zhichao'  
  + 配置邮箱 git config --global user.email'1522554132@qq.com'
  + 生成密钥(公钥和私钥) ssh-keygen -t rsa -C '1522554132@qq.com'
  + 把公钥存在Github上的settings里。
  
## 3. 远程建立新仓库
## 4. 在本地 git remote add origin + 远程仓库地址
  + 报错：remote origin already exists
    + 解决办法  
      1. git remote rm origin
      2. git remote add origin + 远程仓库地址

## 5. 追踪远程分支 git push --set-upstream 本地分支名
## 6. 上传 git push 