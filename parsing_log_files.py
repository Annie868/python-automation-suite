# Scripts for parsing log files to extract specific information or patterns

# Extract lines containing "ERROR"
with open("app.log", "r") as f:
  for line in f:
    if "ERROR" in line:
      print(line.strip())
# This reads the file line by line and prints only those that contain "ERROR".


# Extract specific information with Regex
import re
pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*User login: (\w+)"
with open("app.log", "r") as f:
  for line in f:
    match = re.search(pattern, line)
    if match:
      timestamp, user = match.groups()
      print(f"{timestamp} - {user}")
# Example output: 2025-11-03 - anne


# Count the number of errors
error_count = 0
with open("app.log", "r") as f:
  for line in f:
    if "ERROR" in line:
      error_count += 1
print("Total errors:", error_count)


# Extract IP addresses
import re
pattern = r"(\d+\.\d+\.\d+\.\d+)" #basic IPV4 pattern
with open("network.log", "r") as f:
  for line in f:
    match = re.search(pattern, line)
    if match:
      print(match.group())
# Example output: 192.168.1.10


```
Tips:
- Use .split() or strip() for simple structured logs.
- Use re (regular expressions) for complex or irregular logs.
- Combine with pandas for structured analysis and CSV reports.
- For huge logs, process files line by line instead of reading the whole file into memory.
```




