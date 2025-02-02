# Linux
## 服务器领域
### LAMP（Linux + Apache + MySQL + PHP）
### LNMP（Linux + Nginx+ MySQL + PHP）

## 系统启动
### 内核引导
BIOS开机自检 —> 读入`/boot`目录下的内核文件
### 运行init
所有进程的起点，需读取配置文件`/etc/inittab`
### 系统初始化
激活交换分区，检查磁盘，加载硬件模块
### 建立终端
### 用户登录系统
命令行登录\ssh登录\图形界面登录

## 快捷键
### `[Tab] `有『命令补全』与『文件补齐』的功能
[Tab]      ## 接在一串指令的第一个字的后面，则为『命令补全』
[Tab]      ## 接在一串指令的第二个字以后时，则为『文件补齐』
### `[Ctrl] + c`可以停止当前程序
### `[Ctrl] + d`相当于输入exit
### `[shift]+{[PageUP]|[Page Down]}`
[Shift]+[Page Up]    ## 往前翻页 
[Shift]+[Page Down]  ## 往后翻页


## 系统目录机构 `ls /`
### 系统启动必须
#### /boot
存放的启动Linux 时使用的内核文件，包括连接文件以及镜像文件。
#### /etc
存放所有的系统需要的配置文件和子目录列表，更改目录下的文件可能会导致系统不能启动。
#### /lib
存放基本代码库（比如c++库），其作用类似于Windows里的DLL文件。几乎所有的应用程序都需要用到这些共享库。
#### /sys
这是linux2.6内核的一个很大的变化。该目录下安装了2.6内核中新出现的一个文件系统 sysfs 。
sysfs文件系统集成了3种文件系统的信息：1. 针对进程信息的proc文件系统 2. 针对设备的devfs文件系统 3. 针对伪终端的devpts文件系统
该文件系统是内核设备树的一个直观反映。
当一个内核对象被创建的时候，对应的文件和目录也在内核对象子系统中被创建。

### 指令集合
#### /bin
存放着最常用的程序和指令
#### /sbin
只有系统管理员能使用的程序和指令。

### 外部文件管理
#### /dev
Device(设备)的缩写, 存放的是Linux的外部设备。
注意：在Linux中访问设备和访问文件的方式是相同的。
#### /media
类windows的其他设备，例如U盘、光驱等等，识别后linux会把设备放到这个目录下。
/mnt：临时挂载别的文件系统的，我们可以将光驱挂载在/mnt/上，然后进入该目录就可以查看光驱里的内容了。

### 临时文件
#### /run
是一个临时文件系统，存储系统启动以来的信息。当系统重启时，这个目录下的文件应该被删掉或清除。如果你的系统上有 /var/run 目录，应该让它指向 run。
#### /lost+found
一般情况下为空的，系统非法关机后，这里就存放一些文件。
#### /tmp：
这个目录是用来存放一些临时文件的。

### 账户
#### /root
系统管理员的用户主目录。
#### /home
用户的主目录，以用户的账号命名的。
#### /usr
用户的很多应用程序和文件都放在这个目录下，类似于windows下的program files目录。
#### /usr/bin
系统用户使用的应用程序与指令。
#### /usr/sbin
超级用户使用的比较高级的管理程序和系统守护程序。
#### /usr/src
内核源代码默认的放置目录。

### 运行过程中要用
#### /var
存放经常修改的数据，比如程序运行的日志文件（/var/log 目录下）。
#### /proc
管理内存空间，虚拟的目录，是系统内存的映射，我们可以直接访问这个目录来，获取系统信息。这个目录的内容不在硬盘上而是在内存里，我们也可以直接修改里面的某些文件来做修改。

### 扩展用的
#### /opt
默认是空的，安装额外软件可以放在这个里面。
#### /srv
存放服务启动后需要提取的数据（不用服务器就是空）

# Linux指令
## `ifconfig`查看网络配置
interfaces config 的缩写，用来查看和配置网络设备
### `ifconfig ens33 up`启动网卡
### `ifconfig ens33 down`关闭网卡

## [Linux命令总览](https://www.runoob.com/linux/linux-command-manual.html)

## [常用Linux指令1](https://blog.csdn.net/OKCRoss/article/details/127055932)

## [常用Linux指令2](https://blog.csdn.net/weixin_43908649/category_12090448.html)

## [常用Linux指令3](https://blog.csdn.net/m0_64776928?type=blog)
