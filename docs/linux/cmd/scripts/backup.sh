#!/bin/bash
sep()
{
    printf -v str "%${1}s" ""
    echo "${str// /$2}"
}
sep 50 =
echo `date --iso-8601=seconds` 'Start Backup'
sep 50 =
# This script is just a sample and you can modify it based on your need.
/usr/bin/rsync -azPv -e "ssh -i /home/chyi/.ssh/id_rsa.pub" yogo@YoGo:~/YoGoDir /srv/dev-disk-by-uuid-671cdfc1-9ed4-4b4b-9966-74197042607d
