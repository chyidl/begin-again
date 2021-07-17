# PostgreSQL Tips


Table of Contents
-----------------

* [How to store dates and times in PostgreSQL](#timestamptz)


timestamptz
-----------
```
--- Check timezone in psql
postgres=# SHOW time zone;
 TimeZone
----------
 Etc/UTC
(1 row)

-- Change timezone value
postgres=# SET TIME ZONE 'Asia/Shanghai';
SET

-- Check new timezone value
postgres=# SHOW time zone;
   TimeZone
---------------
 Asia/Shanghai
(1 row)

# PostgreSQL has six different data types
    timestamp [ (p) ] [ without time zone ] 8 bytes both date and time (no time zone) 1 microsecond
    timestamp [ (p) ] with time zone 8 bytes both date and time, with time zone 1 microsecond
    date 4 bytes date(no time of day) 1 day
    time [ (p) ] [ without time zone ] 8 bytes time of day(no date) 1 microsecond
    time [ (p) ] with time zone 12 bytes time of day(no date), with time zone 1 microsecond
    interval [ fields ] [ p ] time interval 1 microsecond

postgres=# SELECT pg_column_size('2000-01-01 00:00:00 +00:00'::timestamp) as "timestamp byte size", pg_column_size('2000-01-01 00:00:00 +00:00'::timestamptz) as "timestamptz byte size";
 timestamp byte size | timestamptz byte size
---------------------+-----------------------
                   8 |                     8
(1 row)
```

* timestamp vs. timestamptz
> These 2 PostgreSQL data types store date and time in a single filed, the difference is that "timestamptz" converts the value to UTC and "timestamp" doesn't.
```
postgres=# SET TIME ZONE 'UTC';
SET
postgres=# SELECT '2000-01-01 00:00:00 +05:00'::timestamp as "Timestamp without timezone", '2000-01-01 00:00:00 +05:00'::timestamptz as "Timestamp with time zone";
 Timestamp without timezone | Timestamp with time zone
----------------------------+--------------------------
 2000-01-01 00:00:00        | 1999-12-31 19:00:00+00
(1 row)

"timestamp" data type ignores the offset('+05:00') from the original value.
"timestamptz" data type takes into account the offset("+05:00") from the original value.

"timestamp without time zone" ("aka timestamp") means "timestamp offset unaware"
"timestamp with time zone" ("aka timestamptz") means "timestamp offset aware"

1. Using timestamp without time zone (timestamp)

develop=# SELECT ('2000-01-01 00:00:00 +00:00'::timestamp)::timestamptz at time zone 'Asia/Shanghai' as "Shanghai timestamp";
 Shanghai timestamp
---------------------
 2000-01-01 08:00:00
(1 row)

2. Using timestamp with time zone (timestamptz)

develop=# SELECT '2000-01-01 00:00:00 +00:00'::timestamptz at time zone 'Asia/Shanghai' as "Shanghai timestamp";
 Shanghai timestamp
---------------------
 2000-01-01 08:00:00
(1 row)
```
