# Automation

## Backups

I have automated the task of creating tar backups using just a single command that specifies the folder to be backed up and destination of the backup file.

### Usage:
```shell
./backup_archived.sh [folder to be backed up] [destination of backup file]
```

If no arguments or invalid arguments are passed, the script returns the usage of the script.