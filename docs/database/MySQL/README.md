# MySQL
```
docker-compose mysql Using Bitnami images

# MySQL Version -- see which MySQL version your system is running
$ mysqld --version

# MySQL Port -- default port for MySQL is 3306

# MySQL Configuration File
> The MySQL configuration file is located at one of the following locations, on the MySQL database server host:
    1. /opt/bitnami/mysql/conf/my.cnf
    2. /opt/bitnami/mysql/my.cnf

[mysqladmin]
user=chyi

[mysqld]
skip_name_resolve
explicit_defaults_for_timestamp
basedir=/opt/bitnami/mysql
port=3306
tmpdir=/opt/bitnami/mysql/tmp
socket=/opt/bitnami/mysql/tmp/mysql.sock
pid_file=/opt/bitnami/mysql/tmp/mysqld.pid
max_allowed_packet=16M
bind_address=0.0.0.0
log_error=/opt/bitnami/mysql/logs/mysqld.log
character_set_server=utf8
collation_server=utf8_general_ci
plugin_dir=/opt/bitnami/mysql/lib/plugin

[client]
port=3306
socket=/opt/bitnami/mysql/tmp/mysql.sock
default_character_set=UTF8
plugin_dir=/opt/bitnami/mysql/lib/plugin

[manager]
port=3306
socket=/opt/bitnami/mysql/tmp/mysql.sock
pid_file=/opt/bitnami/mysql/tmp/mysqld.pid
!include /opt/bitnami/mysql/conf/bitnami/my_custom.cnf
```

## Table of Contents

* [Slow SQL](#slow_sql)

slow_sql
--------
```
long_query_time:
slowlog: 慢查询日志

chyi in ~ at k8s-master
➜ mysql -h 172.30.1.14  -u root -p
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 45936
Server version: 8.0.26 Source distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# 查询慢SQL是否开启
MySQL [(none)]> show variables like 'slow_query_log%';
+---------------------+-------------------------------------------+
| Variable_name       | Value                                     |
+---------------------+-------------------------------------------+
| slow_query_log      | OFF                                       |
| slow_query_log_file | /bitnami/mysql/data/2ba0209e3340-slow.log |
+---------------------+-------------------------------------------+
2 rows in set (0.012 sec)

MySQL [(none)]>
```
