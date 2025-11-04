# SCRIPTS TO TRACK SYSTEM HEALTH METRICS

# 1. Simple System Monitor
import psutil
import shutil
import datetime from datetime

# Get current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"System Health Report - {timestamp}")
print("-" * 40)

# CPU usage
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage}%")

# Memory usage
memory = psutil.virtual_memory()
print(f"Memory Usage: {memory.percent}% of {round(memory.total / (1024**3), 2)} GB")

# Disk usage
disk = shutil.disk_usage("/")
print(f"Disk Usage: {disk.used // (2**30)} GB used / {disk.total // (2**30)} GB total ({disk.used / disk.total * 100:.2f}%)")

# Uptime
uptime_seconds = psutil.boot_time()
uptime = datetime.now().timestamp() - uptime_seconds
hours = int(uptime // 3600)
print(f"System Uptime: {hours} hours")

print("-" * 40)

"""
Sample Output:
System Health Report - 2025-11-03 13:55:00
----------------------------------------
CPU Usage: 14.5%
Memory Usage: 62.3% of 16.0 GB
Disk Usage: 120GB used / 256 GB total (46.9%)
System Uptime: 12 hours
----------------------------------------
"""



# 2. Adding Alerts
if cpu_usage  > 80:
  print("ALERT: High CPU usage!")
if memory.percent > 85:
  print("ALERT: Memory usage too high!")



"""
Optional Enhancements:
- Send email when CPU/memory >90%
- Store readings in CSV for charting
- Use matplotlib to graph CPU/memory over time
- Send data to monitoring dashboard
- Combine with tools like Prometheus, Grafana.
"""
