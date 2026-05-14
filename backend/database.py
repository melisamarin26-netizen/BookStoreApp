import os
import shutil
import sqlite3
from datetime import datetime

# -------------------------------------------------
# INK AND LEATHER BOOKSTORE APP
# Backup and Recovery System
# -------------------------------------------------

# Database file
DATABASE_FILE = 'ink_and_leather.db'

# Backup folder
BACKUP_FOLDER = 'backups'

# Create backup folder if it does not exist
if not os.path.exists(BACKUP_FOLDER):
    os.makedirs(BACKUP_FOLDER)

# -------------------------------------------------
# CREATE SAMPLE DATABASE
# -------------------------------------------------

def create_database():

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    # Customer table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    ''')

    # Inventory table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            book_id INTEGER PRIMARY KEY,
            title TEXT,
            quantity INTEGER,
            price REAL
        )
    ''')

    # Sales table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            sale_id INTEGER PRIMARY KEY,
            customer_name TEXT,
            book_title TEXT,
            amount REAL
        )
    ''')

    connection.commit()
    connection.close()

    print("Database created successfully")

# -------------------------------------------------
# BACKUP SYSTEM
# -------------------------------------------------

def backup_database():

    # Current date and time
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    # Backup filename
    backup_filename = f'ink_and_leather_backup_{timestamp}.db'

    # Full backup path
    backup_path = os.path.join(BACKUP_FOLDER, backup_filename)

    try:
        # Copy database to backup folder
        shutil.copy(DATABASE_FILE, backup_path)

        print(f"Backup completed successfully")
        print(f"Backup saved to: {backup_path}")

    except Exception as error:
        print("Backup failed")
        print(error)

# -------------------------------------------------
# RESTORE SYSTEM
# -------------------------------------------------

def restore_database(backup_file):

    try:
        # Restore selected backup
        shutil.copy(backup_file, DATABASE_FILE)

        print("Database restored successfully")

    except Exception as error:
        print("Restore failed")
        print(error)

# -------------------------------------------------
# VIEW AVAILABLE BACKUPS
# -------------------------------------------------

def list_backups():

    print("\\nAvailable Backups:\\n")

    backups = os.listdir(BACKUP_FOLDER)

    if not backups:
        print("No backups found")

    for backup in backups:
        print(backup)

# -------------------------------------------------
# RUN SYSTEM
# -------------------------------------------------

create_database()

# Create backup
backup_database()

# Display available backups
list_backups()

# Example restore command
# restore_database('backups/ink_and_leather_backup_2026-05-10_14-30-00.db')
import shutil

DATABASE_FILE = 'ink_and_leather.db'

def restore_database(backup_file):

    try:
        # Replace damaged database
        shutil.copy(backup_file, DATABASE_FILE)

        print("Database restored successfully")

    except Exception as error:
        print("Restore failed")
        print(error)

# Example restore command
restore_database(
    'backups/ink_and_leather_backup_2026-05-11_09-15-12.db'
)
