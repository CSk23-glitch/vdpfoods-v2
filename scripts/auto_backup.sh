#!/bin/bash

# Define the local backup file path
BACKUP_FILE="/root/backup_db/ecommerce_db_latest.archive"

# Ensure the backup directory exists
mkdir -p /root/backup_db

# Take a single mongodump and overwrite the latest archive exclusively
docker exec mongodb_db mongodump -u admin -p S_99_chi_231999 --authenticationDatabase admin --db ecommerce_db --archive > "$BACKUP_FILE"

echo "Backup of ecommerce_db successfully dumped locally to $BACKUP_FILE over the previous snapshot at $(date)."
