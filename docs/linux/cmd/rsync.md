# Rsync
> rsync - a fast, versatile, remote (and local) file-copying tool
> It uses an algorithm that minimizes the amount of data copied by only moving the portions of files that have changed.

```
# Debian/Ubuntu
❯ sudo apt install rsync

# macOS
➜ brew install rsync

传输的双方都必须安装rsync

# -r: 递归
# -a: 除了递归同步以外，还可以同步元信息(比如修改时间、权限)
# -n / --dry-run : 模拟执行的结果
# --delete: 删除只存在于目标目录，不存在于源目录的文件
# --exclude: 制定排除模式, 多个排除模式可以用多个--exclude参数
# --exclude-from: 参数制定文件
# --include: 制定必须同步的文件模式
$ rsync -av --delete source/ destination

# Use Rsync to Sync with a Remote System with a Remote System
# rsync 默认使用SSH进行远程登陆和数据传输
# -e 参数制定SSH 使用的1022端口
# -z: reduce the network transfer by adding compression with the -z option
# -P: combines the flags --progress and --partial
#   --progress: a progress bar for the transfers
#   --partial: allow you to resume interrupted
$ rsync -azPv -e 'ssh -p 1022' username@remote_host:source/ destination

# 增量备份
rsync 可以完成增量备份，也就是默认只复制有变动的文件
```
