#!/bin/bash
if [ "$#" -lt 2 ] || ! [ -d "$1" ] || ! [-d "$2"]; then
    echo "Invalid command"
    echo
    echo "Usage: $0 [folder to backup] [destination of created backup]" >&2
    exit 1
fi
backup_files="$1"


destination="$2"

day=$(date +%A)
hostname=$(hostname -s)
archive_file="$hostname-$day.tgz"

echo "Backing up $backup_files to $destination/$archive_file"
echo

tar czf $destination/$archive_file $backup_files

echo
echo "Backup finished at "
date

ls -lh $destination