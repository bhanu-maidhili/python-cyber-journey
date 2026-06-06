# Day 9: Regular Expressions (Regex)
import re
print("--- Regex IP Extraction ---")

# A messy log line from a server
raw_log = "May 31 08:14:22 server sshd[1289]: Failed password for root from 103.45.67.89 port 33890"

# THE PATTERN:
# \d means "any digit (0-9)"
# {1,3} means "between 1 and 3 of those digits"
#\. means "a literal dot"
# So we are looking for: 1-3 digits, a dot, 1-3 digits, a dot, 1-3 digits, a dot, 1-3 digits.
ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# re.findal() searches the string and returns a list of everything that matches the pattern
extracted_ips = re.findall(ip_pattern, raw_log)

print("Log Line:",raw_log)
# Check if our list has anything in it 
if len(extracted_ips)>0:
  print("CRITICAL: Extracted Attacker IP ->",extracted_ips[0])
else:
  print("No IPs found in this log line.")
  
