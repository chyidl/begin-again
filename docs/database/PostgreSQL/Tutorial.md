# Tutorial


Content of tables
------------------

* [pg_dump and pg_restore](#pg_dump_and_pg_restore)


pg_dump_and_pg_restore
----------------------
```
pg_dump:
> a utility for creating consistent database dumps.

Connection options:
  -d, --dbname=DBNAME      database to dump
  -h, --host=HOSTNAME      database server host or socket directory
  -p, --port=PORT          database server port number
  -U, --username=NAME      connect as specified database user
  -w, --no-password        never prompt for password
  -W, --password           force password prompt (should happen automatically)
  --role=ROLENAME          do SET ROLE before dump

    -n, --schema=SCHEMA          dump the named schema(s) only
    -F, --format=c|d|t|p         output file format (custom, directory, tar, plain text (default))

➜ pg_dump -h localhost -p 1433 -U test -d jarvis_cmdb_prod_mirror -n jarvis_cmdb -F t > jarvis_cmdb.tar
➜ ll
total 327808
-rw-r--r--    1 yogo  staff   154M Jul 19 15:21 jarvis_cmdb.tar


# Restore
➜ psql -h localhost -U postgres -d develop -f jarvis_cmdb.sql -v ON_ERROR_STOP=1
or,
➜ pg_restore -hlocalhost -U db_user -d dump staging_dump.tar
```
