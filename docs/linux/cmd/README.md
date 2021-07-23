# Linux Command Line


### Table of Contents

* [Schedule backup in Linux](#rsync_cron)


rsync_cron
----------
> Configure an automatic backup in Linux now and you will thank yourself in the future.
> The following are the detailed instructions for making an automatic and incremental backup.

* Rsync
> rsync - a fast, versatile, remote (and local) file-copying tool
> It uses an algorithm that minimizes the amount of data copied by only moving the portions of files that have changed.

```
# Debian/Ubuntu (Make sure rsync is installed on both Host A and Host B.)
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

* Crontab
```
$ crontab -e

# Modify /etc/crontab file to schedule the execution of backup script. Add this line to the end of the crontab file:

    0 2 * * * root bash backup.sh       # the script file backup.sh is scheduled to be executed every day at 2:00AM.

The content of the backup.sh script is something like this:
#!/bin/sh

/usr/bin/rsync -avz -e "ssh -i /root/.ssh/id_rsa.pub"  root@A.com:/etc  /var/ServerBackup

# Managing Cron Job Output

# To append a scheduled command's output to a log file, add >> to the end of the command followed by the name and location of a log file of your choosing
* * * * * echo 'Run this command every minute' >> /directory/path/file.log

# Use cron to run a script keep it running in the background, you could redirect the scripts output to an empty location: like /dev/null
# standard error -- represented by (2)
# standard output (>&1)
* * * * * echo 'Run thie command every minute' > /dev/null 2>&1
```
[Backup.sh](./scripts/backup.sh)
