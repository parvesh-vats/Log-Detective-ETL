
import sqlite3
from datetime import datetime

conn = sqlite3.connect("logs.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS error_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        level TEXT,
        message TEXT
    )
''')
conn.commit() # Save the table creation


with open("server_log.txt", "r") as file:
    for linenum, line in enumerate(file, start=1):
        if "ERROR" in line.upper():
            part = line.split("|")
            timestamp = part[0].strip()
            level = part[1].strip()
            message = part[2].strip()

            # The Loading Phase
            cursor.execute(
                "INSERT INTO error_logs (timestamp, level, message) VALUES (?, ?, ?)",
                (timestamp, level, message)
            )


conn.commit() # Save all the inserted errors
conn.close()
print("Success: Errors have been loaded into logs.db")