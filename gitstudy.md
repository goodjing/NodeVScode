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