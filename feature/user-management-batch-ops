"""
USER MANAGEMENT SCRIPTS FOR BATCH OPERATIONS

User management scripts help automate:
- Creating new users
- Deleting inactive users
- Changing passwords
- Assigning users to groups
- Managing permissions
Batch operations mean doing these tasks for many users at once, often from a file like users.csv.

Let's say users.csv contains the following:
username,fullname,password
alice,Alice Johnson,Secure123
bob, Bob Smith,Passw0rd!
charlie,Charlie Brown,Test1234

You want a script that:
- Reads this file
- Creates users automatically
- Optionally assigns them groups or permissions.
"""

# 1. Batch User Creation Script (Linux + Python)
# NB: Creating system users requires admin privileges (sudo)

import csv
import os

# Path to the CSV file
with open("users.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    username = row["username"]
    fullname = row["fullname"]
    password = row["password"]

    print(f"Creating user: {username} ({fullname})")

    # Linux command to add user
    os.system(f"sudo useradd -m -c '{fullname}' {username}")
    os.system(f"echo '{username}:{password}' | sudo chpasswd")

print("Batch user creation complete.")

# useradd :    creates the user
# -m :         creates a home directory
# -c :         adds a comment (full name)
# chpasswd :   sets the password.






# 2. Add Users on Windows System
#On Windows, instead of useradd, you can use PowerShell or net user commands:
import os

users = [
  ("alice", "Secure123"),
  ("bob", "Passw0rd!"),
]

for username, password in users:
  os.system(f'net user {username} {password} /add')





# 3. Deleting Users
users_to_delete = ["bob", "charlie"]

for user in users_to_delete:
  print(f"Deleting user: {user}")
  os.system(f"sudo userdel -r {user}") # -r removes home directory

"""
Output:
Deleting user: bob
Deleting user: charlie
"""


# 4. Batch Password Generate
import random
import string
import os

def generate_password (length=10):
  chars = string.ascii_letters + string.digits
  return ''.join(random.choice(chars) for _ in range(length))

users = ["alice", "bob", "charlie"]

for user in users:
  new_pass = generate_password()
  os.system(f"echo '{user}:{new_pass}' | sudo chpasswd")
  print(f"{user} new password: {new_pass}")

"""
Example Output:
alice new password: D5kLpR7aCw
bob new password: pZ7rK4gX1q
charlie new password: tH6eM9bR2u
"""




# 5. Logging Batch Operations
import datetime

with open("user_log.txt", "a") as log:
  log.write(f"Batch run at {datetime.datetime.now()}\n")
  log.write("Users created: alice, bob, charlie\n\n")





