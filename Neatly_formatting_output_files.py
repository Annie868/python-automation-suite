# MANIPULATING TEXT DATA FOR REPORTING PURPOSES

# 1. Clean and Formatting Text
text = "  Total Sales: $ 1 ,200.50  \n"

# Remove extra spaces and newlines
cleaned = text.strip()

# Replace characters
cleaned = cleaned.replace("$", "").replace(",", "")

# Split into label and value
label, value = cleaned.split(":")
label = label.strip()
value = float(value.strip())

print(label, "=", value)

"""
Output: 
  Total Sales = 1200.5
"""


# 2. Working with Multi-line Text

#Suppose you have a log-like text:
# Data = 
"""
Name: Alice, Sales: 1200
Name: Bob, Sales: 1500
Name: Charlie, Sales: 900
"""

# You can extract and process it easily:
report = []
for line in data.splitlines():
  parts = line.split(",")
  name = parts[0].split(":")[1].strip()
  sales = int(parts[1].split(":")[1].strip())
  report.append((name, sales))

print(report)

"""
Output:
[('Alice', 1200), ('Bob', 1500), ('Charlie', 900)]
