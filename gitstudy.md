https://www.cnblogs.com/schaepher/p/5561193.html

### 本地Git使用

#### 新的仓库

- 在本地文件夹鼠标右键点击Git Bash Here 打开窗口
- 运行 git init 初始化仓库
- 文件夹中创建一个文件后，运行 git status 查看变化

![初始化仓库](E:\NodeVScode\picgit\image-20221114095435236.png)

- 有一个还未追踪的文件，并提示可以使用 `git add <file>...` 把它加进去，运行git add -A ， 然后运行 git status

- 看到提示：Changes to be committed，说明可以执行commit

- 运行 git commit -m "提交信息"，将文件提交到repository里

- 运行 git log , 可以查看提交的记录

  > - 如果文件名是中文，运行 git status 会乱码：
  >
  >   若要使其显示中文，执行：git config --global core.quotepath false，再执行 git status 
  >
  > - 如果 git log 也会乱码：
  >
  >   git config --global i18n.commitencoding utf-8 git config --global i18n.logoutputencoding utf-8
  >
  >   

#### 文件添加和提交

- 修改文件保存后，运行 git status 查看变化
- 运行 git diff 查看文件变化具体内容，其默认和最新的commit比较
- 撤销更改：git checkout -- （撤销本地文件）

![文件添加](E:\NodeVScode\picgit\image_20221114102657.png)

#### 版本回退

- 运行 git log，查看版本号
- 开始回退：运行 git reset --hard xxxxxxx （取版本号前七位即可）

![版本回退](E:\NodeVScode\picgit\image_20221114104432.png)

- git reflog，可以看到HEAD的变化情况，随后可以用reset --hard回到最新版本。  

### Git和Github的关联

1. 本地配置用户名和邮箱（已配置过的可以跳过

   git config --global user.name "你的用户名"

   git config --global user.email "1611767852@qq.com"

2. 生成 ssh key

   运行 ssh-keygen -t rsa -C "1611767852@qq.com"

   将生成的 ssh key 复制到剪贴板后执行 clip < ~/.ssh/id_rsa.pub

3. 打开Github，进入settings，点击左边的 SSH and GPG keys后，将ssh key 粘贴到右边的Key中，点击Add SSH key后添加成功。

4. 在Git Bash Here中执行 ssh -T git@github.com 即可。

5. 创建远程仓库与本地关联：github中，点击右上角加号，New repository，接着输入远程仓库名，点击Create repository创建好。

6. 现在Github上复制远程仓库的SSH地址，然后执行：

   git remote add origin 你复制的地址

7. 如果创建 repository 的时候，加入了 README.md 或者 LICENSE ，需要先执行  git pull origin master

8. 否则执行 git push -u origin master，将本地仓库上传至Github的仓库

9. 上传至git仓库：

   git add -A

   git commit -m "上传至github"

   git push

### 获取其他人的远程仓库

1. 复制别人远程仓库的SSH
2. 执行：git clone 复制的SSH地址
3. 取消掉与别人的仓库远程链接：git remote rm origin 
4. 链接自己的远程链接：git remote add origin xxxxxx
5. 自己的 github 创建一个新的仓库后，git push -u origin master