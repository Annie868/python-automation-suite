# AUTOMATING SYSTEM MAINTENANCE TASKS: LOG ROTATION AND BACKUP PROCEDURES  

# 1. Log Rotation
import os
import shutil
from datetime import datetime

log_file = "app.log"

if os.path.exists(log_file):
  timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
  backup_name = f"app_{timestamp}.log"
  
  # Move and rename the old log
  shutil.move(log_file, backup_name)
  print(f"Log rotated: {backup_name}")
  
  # Create a new empty log file
  open(log_file, "w").close()
  print("New log file created.")
  
else:
  print("No log file found.")

"""
This script:
- Renames the old log with a timestamp 
- Starts a new empty app.log file
You can schedule this to run daily or weekly using cron (Linux) or Task Scheduler (Windows).
"""




# 2. Automating Backups
import shutil
from datetime import datetime

source = "/home/user/data"
destination = "/home/user/backups"

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_folder = f"{destination}/backup_{timestamp}"

shutil.copytree(source, backup_folder)
print(f"Backup created at: {backup_folder}")

"""
This script:
- Copies an entire directory to a backup folder
- Adds a timestamp to the backup folder name to keep the data versioned by time of backup creation.
"""



# 3. Automating with Cron (Linux/Mac)
# Save no.2 script as backup_script.py
# Open cron table
crontab -e
#Example cron entry to rotate logs every day at midnight:
0 0 * * * /usr/bin/python3 /home/user/scripts/backup_script.py

# 4. Automating on Windows
"""
- Open Task Scheduler
- Create a new task
- Choose "Run daily" or any interval you prefer
- Set the command: python "C:\path\to\backup_script.py"
"""




# 5. Combining Log Rotation + Backup
import os, shutil, gzip
from datetime import datetime

log_file = "app.log"
backupdir = "backups"
os.makedirs(backup_dir. exist_ok=True)

# Rotate and compress log
if os.path.exists(log_file):
  timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
  rotated = f"{backup_dir}/app_{timestamp}.log"
  shutil.move(log_file, rotated)
  
  # Compress
  with open(rotated, "rb") as f_in, gzip.open(rotated + ".gz", "wb") as f_out:
    shutil.copyfileobj(f_in, f_out)
  os.remove(rotated)

  print(f"Log rotated and compressed to {rotated}.gz")
else:
  print("No log file found.")




"""
Best Practices:
- Use timestamps in filenames: To avoid overwriting old backups
- Compress old logs (gzip): To save disk space
- Automate with cron or Task Scheduler: No manual work needed
- Log automation results: To help you debug failures
- Test your script: To prevent accidental data loss.
"""





  
